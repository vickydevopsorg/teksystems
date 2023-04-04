from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api1')
def api1():
    response = requests.get('http://factorial:5000/factorial?n=5')
    return jsonify(response.json())

@app.route('/api2')
def api2():
    response = requests.get('http://square:5000/square?n=5')
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
