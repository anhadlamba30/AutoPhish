# 🛡️ AutoPhish — Intelligent Email Threat Classifier 
AutoPhish is an AI-powered email classification prototype that detects phishing attempts using an LLM backend. It's designed to be seamlessly integrated into enterprise email systems and security workflows.

## 📷 Demo

![Phising example](screenshots/Not_Phishing_2.png)
![Non-Phishing example](screenshots/Phishing_1.png)


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
```

## 🧭 Future Vision

AutoPhish isn't just a demo — it's a security assistant roadmap.

- 🧩 Outlook Plugin: Direct integration with enterprise Outlook environments

- 🛠️ Tool-Calling LLM: To trigger actions like auto-reply, quarantine, IT report

- 🧠 Agentic Workflows: The LLM can remember flagged threads and user patterns

- 🗂️ Archival & Search: Automatic archiving and tagging of safe conversations

- 🌐 SOC Integration: Plug into existing security orchestration systems (SOAR)
