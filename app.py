from flask import Flask, request, render_template
from json import dumps as json_dumps
from requests import get as request_get
from random import randint, choice as random_choice

app = Flask(__name__)

def randomString(start, end):
    randomInt = randint(start, end)
    string = "_-1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    token = ""
    for i in range(randomInt):
        token += random_choice(string)
    return token

@app.route("/")
def home():
    url = request.path
    return render_template("error404.html", url=url), 404

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if "password" in request.form and "url" in request.form and "ext" in request.form:
        password = request.form.get("password")
        if password != "filedelivr102":
            data = {
                "status": "failure",
                "message": "password is incorrect"
            }
        else:
            url = request.form.get("url")
            extension = request.form.get("ext")
            contents = request_get(url).text
            randomStr = randomString(10, 16)
            serverFileLocation = "static/" + randomStr + "." + extension
            with open(serverFileLocation, "wb") as f:
                f.write(contents)
            httpFileLocation = "http://static-music-matrix.herokuapp.com/" + serverFileLocation
            data = {
                "status": "success",
                "file_url": httpFileLocation
            }
    else:
        data = {
            "status": "failure",
            "message": "method not allowed"
        }
    response = app.response_class(
        response=json_dumps(data),
        status=200,
        mimetype="application/json"
    )
    return response

@app.errorhandler(404)
def errorpage(error):
    url = request.path
    return render_template("error404.html", url=url), 404

app.run(debug=True)