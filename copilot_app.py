import streamlit as st
from openai import OpenAI

# Connect to your local LM Studio server
client = OpenAI(
    base_url="http://192.168.0.106:1234/v1",  # change if needed
    api_key="lm-studio"
)

model_name = "qwen/qwen3-4b-thinking-2507"
system_prompt = "You are a smart and friendly AI Copilot. Help the user with code, reasoning, and creative tasks."

# Streamlit setup
st.set_page_config(page_title="Local AI Copilot", page_icon="🤖", layout="wide")
st.title("Your Personal AI Copilot")
st.caption("Chat with your local model — running privately on your computer!")

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# Chat input
if user_input := st.chat_input("Type your message..."):
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=model_name,
        messages=st.session_state.messages
    )

    msg = response.choices[0].message.content.strip()
    st.chat_message("assistant").write(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})


