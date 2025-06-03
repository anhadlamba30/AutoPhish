# 🛡️ AutoPhish — Intelligent Email Threat Classifier 
AutoPhish is an AI-powered email classification prototype that detects phishing attempts using an LLM backend. It's designed to be seamlessly integrated into enterprise email systems and security workflows.

## 📷 Demo

![AutoPhish Screenshot](screenshots/phishing_detected.png)

## 🚀 Features

- 📧 **Paste Email Content**: Simulate an incoming email.
- 🤖 **LLM-based Detection**: Uses a large language model to classify emails as "Phishing" or "Not Phishing".
- ⚡ **Instant Action**: 
  - ✅ If *not phishing*: Archive + auto-response simulated.
  - ⚠️ If *phishing*: Simulated report to IT Security.

## 🧠 How It Works

- Built with **Streamlit** for rapid prototyping.
- Email content is passed to an **LLM (e.g., LLaMA 3)** running locally via **Ollama** or **LM Studio**.
- The model returns a one-word decision: `"Phishing"` or `"Not Phishing"`.

## 🔧 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/) or [LM Studio](https://lmstudio.ai/)
- Python, requests

## 📦 Local Setup

```bash
git clone https://github.com/yourusername/autophish.git
cd autophish
streamlit run app.py
