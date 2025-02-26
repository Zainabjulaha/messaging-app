from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
