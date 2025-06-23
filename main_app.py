import streamlit as st
import requests

st.title("🤖 Hugging Face Chat Assistant")

user_input = st.text_input(You, )

if user_input
    API_URL = httpsapi-inference.huggingface.comodelsmeta-llamaMeta-Llama-3-8B-Instruct
    headers = {Authorization fBearer {st.secrets['HF_TOKEN']}}
    payload = {inputs user_input}
    
    response = requests.post(API_URL, headers=headers, json=payload)

    try
        result = response.json()
        output = result[0]['generated_text']
        st.markdown(fAssistant {output})
    except
        st.error(Something went wrong with the Hugging Face API.)
