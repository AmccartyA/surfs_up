from flask import Flask

#Create Instance
app = Flask(__name__)

#Create Route
@app.route('/')
def hello_world():
    return 'Hello World you Big Beautiful Idiot'