from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(64), index=True, unique=True)
    receipt_text = db.Column(db.String(1000), index=True)
    ingredients = db.relationship("Ingredient", backref="?????", lazy="dynamic")

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    receipt_id = db.Column(db.Integer, db.ForeignKey("receipt.id"))