from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Rule-based responses for customer support queries
responses = {
    "hello": ["Hi! How can I assist you today?", "Hello! Need help with something?", "Hey there! How can I help?"],
    "order status": ["Please provide your order ID so I can check the status.", 
                     "To check your order status, I’ll need your order number."],
    "refund": ["We’re sorry to hear that. Refunds are typically processed within 5–7 business days.", 
               "You can request a refund via your order page. Let me know if you need help!"],
    "return policy": ["You can return items within 30 days of purchase. Visit our returns page for more info.", 
                      "Our return policy allows returns within 30 days. Need help with a return?"],
    "shipping": ["Shipping usually takes 3–5 business days.", 
                 "Standard shipping is 3–5 business days. Do you want to track your order?"],
    "contact support": ["You can reach our support team at support@example.com or call 1800-123-456.", 
                        "Our support team is available via chat and email!"],
    "thank you": ["You're welcome! Is there anything else I can help with?", "Happy to help!"],
    "bye": ["Goodbye! Have a great day!", "Take care! Reach out if you need anything else."],
    "default": ["I'm sorry, I didn't understand that. Could you please rephrase?", 
                "Can you clarify your question about our services or policies?"]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"].lower()

    # Match based on keywords
    for keyword in responses:
        if keyword in user_input:
            return jsonify({"response": random.choice(responses[keyword])})
    
    return jsonify({"response": random.choice(responses["default"])})

if __name__ == "__main__":
    app.run(debug=True)
