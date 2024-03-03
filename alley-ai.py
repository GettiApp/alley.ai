# alley_bot.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a simple chatbot response
def chatbot_response(user_input):
    # Replace this with your actual chatbot logic
    return f"Alley.ai says: You said '{user_input}'"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
