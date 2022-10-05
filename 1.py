import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        data = request.json
        print(data)
        with open ("users.json", "a", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return '200'

    if request.method == 'GET':
        data = request.json
        return data
        

@app.route('/api/get/', methods=['DELETE', 'PUT'])
def get():
    pass


if __name__ == "__main__":
    app.run(port=3005)