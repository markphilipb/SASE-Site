from app import app
from flask import render_template, request
from app.email import send_email
from flask_mail import Mail, Message
from app import mail


@app.route('/')
@app.route('/index')
def index():
    return render_template('startbootstrap-grayscale-gh-pages/index.html', title='SASE')


@app.route('/albums')
def albums():
    return render_template('startbootstrap-grayscale-gh-pages/albums.html', title='SASE')


@app.route('/email', methods=['GET', 'POST'])
def email():
    text = request.form['inem']
    send_email('Add me to the list serv please', 'kungfucut1@gmail.com', ['ubsase@gmail.com'], 'body', '<p>' + text + '</p>')
    return render_template('startbootstrap-grayscale-gh-pages/index.html', title='SASE')
