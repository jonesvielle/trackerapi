import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('service_account_key.json')

# print(cred_obj)
firebase_admin.initialize_app(
    cred_obj, {'databaseURL': 'https://tracker-a8d00-default-rtdb.firebaseio.com/'})

ref = db.reference('/locations')
data = {

    "longitude": 6,
    "latitude": 4,
    "device_id": "66564-adecedded"

}

bookRef = ref.push().set(data)
# bookRef.delete()

# print(ref.get())
# locations = ref.get()
# for i in locations:
#     print(locations[i])
