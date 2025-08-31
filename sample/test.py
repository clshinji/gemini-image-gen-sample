# from IPython.display import Image, Markdown, display
from google import genai
from google.genai.types import GenerateContentConfig, Part
from dotenv import load_dotenv
load_dotenv()

PROJECT_ID = "gen-lang-client-0112356509"
LOCATION = "global"


client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
MODEL_ID = "gemini-2.5-flash-image-preview"
response = client.models.generate_content(
    model=MODEL_ID,
    contents=("generate an image of a cow."),
    config=GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        candidate_count=1,
    ),
)

for part in response.candidates[0].content.parts:
    # if part.text:
    print(part.text)
    # elif part.inline_data:
    #     display(Image(data=part.inline_data.data, width=350, height=350))
