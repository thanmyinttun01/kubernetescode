from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Ko than myint tun , Please subscribe, like, and comment on this video, TY!!!'
