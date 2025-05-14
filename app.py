from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def mars1():
    return "Миссия Колонизация Марса"


@app.route('/carousel')
def sample_file_upload():
    return render_template('carousel.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
