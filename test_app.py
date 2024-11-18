"""
Author : Janarddan Sarkar
file_name : test_app.py 
date : 19-11-2024
description : 
"""
from app import app

def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data== b"Hello World!"

# '''
# Code Breakdown:
# from app import app:
#
# Imports the app object from the app module. This is the Flask application instance being tested.
# def test_home()::
#
# Defines the test function test_home(). This function uses Flask's built-in testing client to perform the test.
# response = app.test_client().get("/"):
#
# Creates a test client using app.test_client().
# Sends a GET request to the root URL ("/") of the application.
# Stores the response from the server in the response variable.
# assert response.status_code == 200:
#
# Asserts that the HTTP status code of the response is 200.
# A 200 status code indicates a successful request, so this test checks that the server responded correctly to the request.
# assert response.data == b"Hello World!":
#
# Checks that the response body (stored in response.data) is exactly equal to the byte string b"Hello World!".
# Flask responses return data in the form of byte strings, so the expected response is written as a byte string (prefixed with b).
# '''