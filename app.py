# from crypt import methods
from flask import Flask, request, Response
from flask import jsonify, session
from user.models import User
from flask_cors import CORS, cross_origin
# from flask_session import Session

app = Flask(__name__)
# app.config['UPLOAD_FOLDER']
app.secret_key = 'jones'
# app.config['SESSION_TYPE'] = 'filesystem'
# app.config["SESSION_PERMANENT"] = False
CORS(app)


@app.route('/')
def home():
    return jsonify({"message": "flask running"})


@app.route('/api/login_device/', methods=['POST'])
def login_device():
    return User().login_device()


@app.route('/api/register_device/', methods=['POST'])
def register_device():
    return User().register_device()


@app.route('/api/push_location/<device_id>/<longitude>/<latitude>/', methods=['GET'])
def push_location(device_id, longitude, latitude):
    return User().push_location(device_id=device_id, latitude=latitude, longitude=longitude)


if __name__ == '__main__':
    app.run(debug=True)
