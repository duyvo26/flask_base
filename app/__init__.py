from flask import Flask
from app.config import Settings
from app.routes import main, auth


def create_app():
    app = Flask(__name__)
    app.config.from_object(Settings)

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    return app
