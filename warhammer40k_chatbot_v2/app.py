from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your environment variables or .env file.")

client = OpenAI(api_key=api_key)

app = Flask(__name__)

SYSTEM_PROMPT = """You are a Warhammer 40K lore expert.
Speak in a grimdark tone. Use provided lore when relevant."""

with open("lore.json", "r") as f:
    LORE = json.load(f)

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def search_lore(query):
    results = []
    for key, value in LORE.items():
        if query.lower() in key.lower() or query.lower() in value.lower():
            results.append(f"{key}: {value}")
    return results

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    # 🔍 RAG: hae relevant lore
    lore_results = search_lore(user_input)
    lore_text = "\n".join(lore_results)

    context_message = {
        "role": "system",
        "content": f"Relevant lore:\n{lore_text}" if lore_text else "No relevant lore."
    }

    messages = conversation_history + [context_message, {"role": "user", "content": user_input}]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content

        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": reply})

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"❌ Error: {type(e).__name__}: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
