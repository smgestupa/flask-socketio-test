import os
from flask import Flask

from .events import socketio
from .routes import chat

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.register_blueprint(chat)

    socketio.init_app(app)

    return app