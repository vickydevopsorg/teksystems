from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/square')
def factorial():
    n = int(request.args.get('n'))
    result = math.pow(n,2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
