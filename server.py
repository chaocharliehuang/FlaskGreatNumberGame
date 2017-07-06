from flask import Flask, render_template, redirect, session, request, jsonify

import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    session['random'] = str(random.randrange(1, 11))
    return render_template('index.html')

@app.route('/<guess>')
def process_guess(guess):
    if guess == session['random']:
        return jsonify(result='correct', text=' was the number!', color='green', number=session['random'])
    elif guess > session['random']:
        return jsonify(result='wrong', text='Too high!', color='red')
    else:
        return jsonify(result='wrong', text='Too low!', color='red')

app.run(debug=True)