from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

from .models import User, Post

# ensure that the necessary database tables are created within the Flask application context
with app.app_context():
    db.create_all()

