from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Ko than myint! , Welcome to our Channel Web Site!'
