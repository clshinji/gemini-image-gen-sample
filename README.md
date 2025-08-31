# Gemini 2.5 Flash Image Generator

このアプリケーションは、GoogleのGemini 2.5 Flashモデルを使用して、テキストプロンプトや画像から新しい画像を生成するStreamlitアプリケーションです。

## 概要

ユーザーはテキストプロンプトを入力し、オプションで画像をアップロードすることで、AIによる画像生成を行うことができます。生成された画像はチャット形式で表示され、ローカルに保存することも可能です。

## 機能

*   テキストプロンプトからの画像生成
*   画像とテキストプロンプトを組み合わせた画像生成
*   チャット形式のUI
*   生成された画像の保存

## 必要なもの

*   Python 3.7以上
*   Google Cloud プロジェクトID
*   Vertex AI APIの有効化

## インストールと実行方法

1.  **リポジトリをクローンします。**
    ```bash
    git clone https://github.com/your-username/gemini-2-5-flash-image.git
    cd gemini-2-5-flash-image
    ```

2.  **必要なライブラリをインストールします。**
    ```bash
    pip install -r requirements.txt
    ```

3.  **環境変数を設定します。**
    `.env.sample` ファイルをコピーして `.env` を作成し、ご自身のGoogle CloudプロジェクトIDを記述してください。

    ```
    GOOGLE_APPLICATION_CREDENTIALS="your-gcp-credentials.json"
    ```

4.  **Streamlitアプリケーションを実行します。**
    ```bash
    streamlit run app.py
    ```

## 設定

*   `PROJECT_ID`: ご自身のGoogle CloudプロジェクトIDに書き換えてください。
*   `MODEL_ID`: 使用するモデルIDです。デフォルトは `gemini-2.5-flash-image-preview` です。

## 使い方

1.  アプリケーションを起動すると、チャットウィンドウが表示されます。
2.  テキスト入力ボックスに、生成したい画像の説明（プロンプト）を入力します。
3.  （オプション）サイドバーのファイルアップローダーを使って、ベースとなる画像をアップロードできます。
4.  入力後、Enterキーを押すと画像生成が開始されます。
5.  生成された画像がチャットに表示されます。

## サンプル

* sample ディレクトリにテスト用の画像とプロンプトがあります。

