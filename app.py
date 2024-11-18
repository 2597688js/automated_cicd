"""
Author : Janarddan Sarkar
file_name : app.py 
date : 19-11-2024
description : 
"""
from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
