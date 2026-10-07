from flask import Flask, render_template
from db import hentedata

app = Flask(__name__)


@app.route("/")
def index():
    print("Dette skriver jeg ut med print")
    return render_template("index.html")

@app.route("/Jinja")
def jinja():
    navn = "Zakaria"
    elever = ["Ola", "Kari", "Per", "Fatima"]
    return render_template("jinja.html", navn=navn, elever=elever)

@app.route("/flasker")
def flasker():
    data = hentedata()
    return render_template("flasker.html", flasker = data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
