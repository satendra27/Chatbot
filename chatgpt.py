from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Configure the generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

# Define a function to get a response from the Gemini model
def get_gemini_response(question: str) -> str:
    response = model.generate_content(question)
    return response.text

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    response = None
    if request.method == 'POST':
        user_input = request.form['input']
        response = get_gemini_response(user_input)
    return render_template('chatbot.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
