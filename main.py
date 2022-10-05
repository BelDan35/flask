import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/post/', methods=['POST'])
def post():
    print('request________', request)
    print('request.form________', request.form)
    if request.method == 'POST':
        data = request.form
        json_dumps = json.dumps(data, ensure_ascii=False)
        print('json_dumps__________', json_dumps)
        with open("users.json", "a") as file:
            json.dump(json_dumps, file, ensure_ascii=False, indent=2)
            file.write(',\n')
        with open("users.json", "r") as f:
            print(*f)
    return 'пользователь добавлен'

@app.route('/api/get/', methods=['GET'])
def get():
    pass

if __name__ == "__main__":
    app.run(port=3005)