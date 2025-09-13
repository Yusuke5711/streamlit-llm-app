from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.markdown("""
# 専門家チャットアプリ

このアプリでは、家電量販店の店員または本屋の店員として、質問に回答します。
1. 「専門家の種類を選択してください」から店員の種類を選びます。
2. 「質問を入力してください」に質問を入力すると、選択した専門家が回答します。
""")

expert_type = st.radio(
    "専門家の種類を選択してください",
    ("家電量販店の店員", "本屋の店員")
)

def get_llm_response(input_text, expert_type):
    if expert_type == "家電量販店の店員":
        system_message = "あなたは優秀な家電量販店の店員です。"
    else:
        system_message = "あなたは優秀な本屋の店員です。"
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]
    result = llm(messages)
    return result.content

input_text = st.text_input("質問を入力してください")
if input_text:
    response = get_llm_response(input_text, expert_type)
    st.write(response)
