from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'blockchain.cmpe281',
    MAIL_PASSWORD = 'Qwerty@281',
    MAIL_DEBUG = True
)
mail=Mail(app)

@app.route("/")
def index():
    msg = Message("Hi! Welcome to Flask Mail!", sender='blockchain.cmpe281', recipients=['patel.farhaaan@gmail.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    return "Sent"

if __name__ == "__main__":
    app.run()