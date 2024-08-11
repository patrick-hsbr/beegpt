from flask import Flask, render_template, request
import openai
import ssl
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from a .env file
load_dotenv()

# Custom adapter to ignore SSL certificate verification
class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        kwargs['ssl_context'] = context
        return super(SSLAdapter, self).init_poolmanager(*args, **kwargs)

# Function to get the API key from an environment variable
def get_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")
    return api_key

# Set your OpenAI API key
openai.api_key = get_api_key()

# Create a session and mount the SSLAdapter to disable SSL verification
session = requests.Session()
session.mount('https://', SSLAdapter())

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form.get("message")
        if user_message:
            try:
                response = session.post(
                    'https://api.openai.com/v1/chat/completions',
                    json={
                        "model": "gpt-3.5-turbo",
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are BeeGPT. You are a specialized assistant."
                            },
                            {"role": "user", "content": user_message}
                        ],
                        "max_tokens": 1000  # Adjusted for an approximate max of 2500 characters
                    },
                    headers={
                        "Authorization": f"Bearer {openai.api_key}",
                        "OpenAI-Beta": "assistants=v2"
                    }
                )
                
                if response.status_code == 200:
                    chatgpt_response = response.json()['choices'][0]['message']['content']
                    response_trimmed = False
                    if len(chatgpt_response) > 2500:
                        chatgpt_response = chatgpt_response[:2500]
                        response_trimmed = True
                    return render_template("index.html", user_message=user_message, chatgpt_response=chatgpt_response, response_trimmed=response_trimmed)
                else:
                    error_message = f"Error: {response.status_code}, {response.text}"
                    return render_template("index.html", error_message=error_message)
            
            except requests.exceptions.SSLError as e:
                return render_template("index.html", error_message=f"SSL error occurred: {e}")
            except Exception as e:
                return render_template("index.html", error_message=f"An error occurred: {e}")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
