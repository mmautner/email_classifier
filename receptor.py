#!/usr/bin/env python

import json
import requests

from sklearn.externals import joblib

from secret import PUSHOVER_TOKEN
from secret import PUSHOVER_USER

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    body = request.form['stripped-text']
    headers = [header[0] for header in json.loads(request.form['message-headers'])]
    full_body = body + ' ' + ' '.join(headers)

    # load model, vectorizer
    model = joblib.load('email_importance.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    vector = vectorizer.transform([full_body])[0]

    if model.predict(vector):
        # any push-notification service could go here
        d = {
             "token":  PUSHOVER_TOKEN,
             "user": PUSHOVER_USER,
             "message": (request.form.get('Subject', 'No Subject: ') + full_body)[:400]
        }
        r = requests.post("https://api.pushover.net/1/messages.json", params=d)
        print r.content

    print body

    return 'OK', 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
