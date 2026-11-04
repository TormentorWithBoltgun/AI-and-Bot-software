# ⚔️ Warhammer 40K AI Chatbot (RAG)

## 📜 Overview

This project is a Warhammer 40K–themed AI chatbot that answers user questions in a grimdark tone.
It combines a local lore database with an AI language model using a Retrieval-Augmented Generation (RAG) approach.

The application is built with a Python backend and a simple web interface using Flask.

---

## 🚀 Features

* AI-powered chatbot (OpenAI API)
* Warhammer 40K themed responses (grimdark style)
* Local lore database (`lore.json`)
* Retrieval-Augmented Generation (RAG)
* Conversation memory
* Web-based user interface (Flask)

---

## 🧠 How It Works

1. The user sends a message via the web interface
2. The application searches for relevant entries in `lore.json`
3. Matching lore is injected into the AI context
4. The AI generates a response using both:

   * the language model
   * the retrieved lore data

This improves response accuracy and relevance.

---

## 🛠️ Tech Stack

* Python
* Flask
* OpenAI API
* HTML / CSS
* JSON (for local data storage)

---

## ⚙️ Installation

1. Clone the repository:

```
git clone <your-repo-url>
cd <project-folder>
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory "if not already there"
	or Copy .env.example to .env and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the application:

```
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

Start chatting with the AI.

---

## 🔐 Notes

* A valid OpenAI API key is required
* The `.env` file should NOT be included in version control
* Use `.env.example` for sharing configuration
* !!!Do NOT leak your OPENAI_API_KEY, that you inserted in .env-file!!! 
	To share the project either DELETE the .env or rewrite/censor your .env like
	OPENAI_API_KEY=your_api_key_here

---

## 📁 Project Structure

```
app.py              # Main Flask application  
lore.json           # Local lore database  
templates/          # HTML frontend  
static/             # CSS styles  
requirements.txt    # Dependencies  
.env.example        # Example environment config  
```


---

## 👨‍💻 Author

Keni Suomalainen

---

## ⭐ Why This Project

This project demonstrates:

* AI integration in applications
* Use of RAG (Retrieval-Augmented Generation)
* Full-stack development (backend + frontend)
* Secure API key handling

---
