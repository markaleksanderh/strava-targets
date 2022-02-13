from flask import (
    Flask,
    jsonify,
    render_template,
)

import os

STRAVA_CLIENT_ID = os.environ.get('STRAVA_CLIENT_ID')
STRAVA_CLIENT_SECRET = os.environ.get('STRAVA_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ['SECRET_KEY']

    @app.route('/')
    def index():
        return render_template('index.html')

    return app 