from flask import Flask, render_template

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

@app.route("/endeenside")
def endeenside():
    return render_template("endeenside.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)