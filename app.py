from flask import Flask, render_template
from requests import *

app = Flask(__name__)


@app.route('/')
def mars1():
    return "Миссия Колонизация Марса"


@app.route('/astronaut_selection')
def two_params(nickname, level=0, rating=0.0):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)