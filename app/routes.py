from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('startbootstrap-grayscale-gh-pages/index.html', title='SASE')


@app.route('/albums')
def albums():
    return render_template('startbootstrap-grayscale-gh-pages/albums.html', title='SASE')
