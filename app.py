from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from google import genai
from google.genai.types import Part, GenerateContentConfig, Blob
import os
import time

# Initialize Vertex AI
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = "global"
client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
MODEL_ID = "gemini-2.5-flash-image-preview"

# Create temp_images directory if it doesn't exist
os.makedirs("temp_images", exist_ok=True)

st.title("Gemini 2.5 Flash Image Generator")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if isinstance(message["content"], str):
            st.markdown(message["content"])
        else:
            for part in message["content"]:
                if "text" in part and part["text"]:
                    st.markdown(part["text"])
                elif "image" in part and part["image"]:
                    st.image(part["image"], caption="Generated Image")

# Add a file uploader to the sidebar
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    content = [prompt]
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        image_part = Part(
            inline_data=Blob(data=image_data, mime_type=uploaded_file.type)
        )
        content.append(image_part)

    # Generate image
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=content,
            config=GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
                candidate_count=1,
            ),
        )

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            assistant_response_parts = []
            for part in response.candidates[0].content.parts:
                if part.text:
                    st.markdown(part.text)
                    assistant_response_parts.append({"text": part.text})
                elif part.inline_data:
                    image_data = part.inline_data.data
                    mime_type = part.inline_data.mime_type
                    extension = mime_type.split("/")[-1]

                    # Sanitize extension
                    if extension not in ["png", "jpg", "jpeg", "gif", "webp"]:
                        extension = "png"  # default to png if mime type is weird

                    filename = f"temp_images/img_{int(time.time_ns())}.{extension}"

                    with open(filename, "wb") as f:
                        f.write(image_data)

                    st.image(
                        image_data, caption=f"Generated Image (saved as {filename})"
                    )
                    assistant_response_parts.append({"image": image_data})

        # Add assistant response to chat history
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_response_parts}
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")
