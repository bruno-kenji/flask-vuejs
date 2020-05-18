from flask import Flask, render_template, jsonify
from random import randint
from flask_cors import CORS
from requests import get

app = Flask(__name__,
            static_folder="./vuejs-flask/dist/static",
            template_folder="./vuejs-flask/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/random', methods=['GET', 'POST'])
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
