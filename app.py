import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>大吉</h1><p>八幡平の山に登ると、いいことがあります</p>"


@app.route("/hello/<name>")
def hello(name):
    return f"<p>こんにちは{name}</p>"


@app.route("/omikuji")
def omikuji():
    results = ["大吉", "中吉", "小吉", "吉", "凶"]

    result = random.choice(results)

    return f"あなたの運勢は{result}です"
