from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> Deployed to Heroku</h1>"

@app.route("/favicon.ico")
def favicon():
    return redirect("/")

if __name__ == "__main__":
    app.run()