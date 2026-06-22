
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY") )
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]

    prompt = f"""
You are x.AI.

Rules:
- your founder name is sunny
- Your name is x.AI
- You are a private AI assistant
- Keep answers clear and helpful

User: {user_message}
"""

    try:
        response = model.generate_content(prompt)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "reply": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True)