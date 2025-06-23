import streamlit as st
import requests

st.title("🤖 Hugging Face Chat Assistant")

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        output = query({"inputs": user_input})
        try:
            generated_text = output[0]["generated_text"]
            st.write(f"**Assistant:** {generated_text}")
        except:
            st.error("⚠️ Error from Hugging Face API. Check your model or token.")
