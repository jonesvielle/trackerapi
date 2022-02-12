from flask import Flask, jsonify, request, session
from passlib.hash import pbkdf2_sha256
# from werkzeug.utils import secure_filename
# from bigchaindb_driver import BigchainDB
# from bigchaindb_driver.crypto import generate_keypair
import uuid
import pymongo
import datetime
import random
import string
import json
import jwt
import firebase_admin
from firebase_admin import db
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

cred_obj = firebase_admin.credentials.Certificate('service_account_key.json')
firebase_admin.initialize_app(
    cred_obj, {'databaseURL': os.getenv('DATABASEURL')})

# from bson.json_util import dumps, loads
# from bson import ObjectId
# from paystackapi.transfer import Transfer
# from paystackapi.transfer import Transfer
conn_string = os.getenv('MONGODBCONNECTIONSTRING')
client = pymongo.MongoClient(conn_string)
databaseConn = client.dataiot


class User:
    def get_random_string(self, length):
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits)
                              for i in range(length)))
        return result_str

    def login_device(self):
        _json = request.json
        _device_id = _json['device_id']
        _phone = _json['phone']
        _pin = _json['pin']
        if databaseConn.track_users({"device_id": _device_id, "phone": _phone, "pin": _pin}):
            return jsonify({"message": "access granted"}), 200
        return jsonify({"message": "access denied"}), 401

    def push_location(self, device_id, latitude, longitude):
        ref = db.reference('/locations')
        data = {
            "device_id": device_id,
            "latitude": latitude,
            "longitude": longitude
        }
        try:
            ref.push().set(data)
        except Exception as e:
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "sent successfully"}), 200
        # return jsonify({"message": "something went wrong"}), 500
