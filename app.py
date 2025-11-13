import streamlit as st
from openai import OpenAI

client = OpenAI(base_url="http://192.168.0.106:1234/v1", api_key="lm-studio")
MODEL="qwen/qwen3-4b-thinking-2507"

st.title("Local Copilot (Browser)")
if "history" not in st.session_state:
    st.session_state.history = []

prompt = st.text_input("You:", "")
if st.button("Send") and prompt:
    st.session_state.history.append(("You", prompt))
    resp = client.chat.completions.create(model=MODEL, messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":prompt}
    ])
    reply = resp.choices[0].message.content
    st.session_state.history.append(("Copilot", reply))

for who, text in st.session_state.history:
    st.markdown(f"**{who}**: {text}")
