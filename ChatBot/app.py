from flask import Flask, request, jsonify, render_template
from chatbot import SmartBudgetAIChatbot
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
chatbot = SmartBudgetAIChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('input', '')
        if not user_input:
            return jsonify({'response': 'Please provide some input.'}), 400
        
        response = chatbot.get_ai_response(user_input)
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'response': 'Sorry, there was an error processing your request.'}), 500

if __name__ == '__main__':
    # Use environment variables for host and port
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
