from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st


# 環境変数のロード
load_dotenv()

# タイトル
st.title("Lesson21 提出課題：LLMアプリ")

st.write("#### あなたのお悩みにAI専門家がアドバイスします。")
st.write("お悩みの種類を選択して、質問内容で入力してください。")

st.divider()
selected_item = st.radio(
    "（１）お悩みの種類を選択してください。",
    ["親の育児ストレスでお悩み", "子供の栄養でお悩み", "子どもの睡眠習慣"]
)

st.divider()
input_text = st.text_input(label="（２）質問内容を入力してください。")


def chat(template, input_text):
    # フォーマット文字列を含むプロンプトを生成
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["input"]
    )
    prompt = prompt_template.format(input=input_text)

    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=prompt)
    ]

    # LLM APIクライアントを生成
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

    return llm(messages)

if len(selected_item) > 0 and len(input_text) > 0:
    match selected_item:
        case "親の育児ストレスでお悩み":
            template1 = """
    あなたは親の育児ストレスを軽減するための専門家です。
    育児疲れやストレス管理に関する実践的なアドバイスを提供します。
    親自身の心身の健康を保つための方法を教えます。

    質問：{input}
    """
            result = chat(template1, input_text)
            st.divider()
            st.write(result.content)

        case "子供の栄養でお悩み":
            template2 = """
    あなたは子どもの栄養に詳しいアドバイザーです。
    子どもの健康な発育を支える食事や栄養バランスについてアドバイスを提供します。
    食事の習慣や偏食に関する質問にも丁寧に答えます。

    質問：{input}
    """
            result = chat(template2, input_text)
            st.divider()
            st.write(result.content)

        case "子どもの睡眠習慣":
            template3 = """
    あなたは子どもの睡眠習慣に詳しい専門家です。
    子どもの夜泣きや睡眠不足に関する解決策を提供し、健全な睡眠を促すためのアドバイスを行います。
    親が子どもの睡眠問題に対処できるようサポートします。

    質問：{input}
    """
            result = chat(template3, input_text)
            st.divider()
            st.write(result.content)

