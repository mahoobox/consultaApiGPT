from flask import Flask, request, render_template
from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN_OPEN_AI')
client = OpenAI(api_key=token)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/respuesta', methods=['POST'])
def get_answer():
    question = request.form['question']
    #response = client.chat.completions.create(model="gpt-3.5-turbo",
    response = client.chat.completions.create(model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ])
    answer = response.choices[0].message.content
    return render_template('index.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)