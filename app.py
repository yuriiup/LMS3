from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/')
def mars1():
    return "Миссия Колонизация Марса"


@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astonaut_selection.html')


@app.route('/results')
def two_params(nickname, level=0, rating=0.0):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


@app.route('/carousel')
def sample_file_upload():
    return render_template('carousel.html')


upload_folder = os.path.join('static', 'img')
app.config['img'] = upload_folder


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['img'], filename))
        img = os.path.join(app.config['img'], filename)
        return render_template('load_photo.html', img=img)
    return render_template('load_photo.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
