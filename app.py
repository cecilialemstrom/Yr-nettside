from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bergen")
def bergen():
    return render_template("bergen.html")

@app.route("/oslo")
def oslo():
    return render_template("oslo.html")

@app.route("/sandvika")
def sandvika():
    return render_template("sandvika.html")

@app.route("/tromsø")
def tromsø():
    return render_template("tromsø.html")


