from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from flask_cors import CORS  # Import Flask-CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def fetch_research_papers(category, topic):
    prompt = f"Find previous research papers related to {topic} in the category {category}. Provide them year-wise with researcher names."
    chat = ChatGroq(model_name="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
    response = chat.predict(prompt)
    return response if response else "Error fetching data from ChatGroq API"

@app.route("/get_research", methods=["POST"])
def get_research():
    data = request.get_json()
    if not data or "category" not in data or "topic" not in data:
        return jsonify({"error": "Please provide category and topic."}), 400
    
    category = data["category"]
    topic = data["topic"]

    result = fetch_research_papers(category, topic)
    return jsonify({"research_papers": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
