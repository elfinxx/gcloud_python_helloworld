from flask import Flask
from flask import request
from flask import jsonify
import os
from slackclient import SlackClient


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Good!?'


@app.route('/event', methods= ['POST'])
def event():
    j = request.get_json()

    if 'challenge' in j:
        print(j['challenge'])
        r = {"challenge": j['challenge']}
        return jsonify(r)
    else:
        print(j['event']['text'])
        return jsonify({"status": "ok"})


@app.route('/slack')
def slack():
    token = ""
    sc = SlackClient(token)
    sc.api_call(
        "chat.postMessage",
        channel="C03E4P03R",
        text="Hello from Python! :tada:"
    )
    return 'Good!?'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

