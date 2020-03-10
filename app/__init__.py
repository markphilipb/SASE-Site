from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.debug = True

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = 1
app.config['MAIL_USERNAME'] = 'kungfucut1@gmail.com'
app.config['MAIL_PASSWORD'] = 'fufufux3'

mail = Mail(app)

from app import routes