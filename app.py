import streamlit as st
import requests
import os

# LLM endpoint (Ollama or LM Studio)
OPENAI_API_URL = "http://localhost:11434/v1/chat/completions"  # change port if needed
MODEL_NAME = "gemma3:12b-it-qat"  # or whatever model you're running

# Load the system prompt
with open("phishing_prompt.txt", "r") as f:
    SYSTEM_PROMPT = f.read()

def call_llm(email_text):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": email_text}
        ],
        "temperature": 0
    }

    response = requests.post(OPENAI_API_URL, json=data, headers=headers)
    result = response.json()
    try:
        return result["choices"][0]["message"]["content"].strip()
    except:
        return "Error"

# Streamlit UI
st.set_page_config(page_title="AutoPhish", page_icon="🛡️")
st.title("🛡️ AutoPhish - Intelligent Email Threat Classifier")

email_input = st.text_area("📧 Paste Email Content Here:", height=250)

if st.button("🔍 Analyze Email"):
    if not email_input.strip():
        st.warning("Please paste some email content.")
    else:
        with st.spinner("Analyzing email..."):
            decision = call_llm(email_input)
        if "phishing" in decision.lower():
            st.error("⚠️ PHISHING DETECTED! Forwarded to IT security team.")
        elif "not" in decision.lower():
            st.success("✅ Not phishing. Archived and responded.")
        else:
            st.warning("🤖 Could not determine. Response unclear.")

st.markdown("---")
st.caption("This is a prototype. LLM classification is simulated.")
