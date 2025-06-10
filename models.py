from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 # Initialisation de SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
 """Représente un utilisateur dans la base de données."""
 id = db.Column(db.Integer, primary_key=True) # ID unique pour chaque utilisateur
 username = db.Column(db.String(80), unique=True, nullable=False) # Nom d’utilisateur unique
 password = db.Column(db.String(120), nullable=False) # Mot de passe haché
 class LostItem(db.Model):
  """Représente un objet perdu."""
 id = db.Column(db.Integer, primary_key=True) # ID unique
 description = db.Column(db.String(200), nullable=False) # Description de l’objet
 date = db.Column(db.DateTime, default=datetime.utcnow) # Date de déclaration
 user_id = db.Column( db.Integer, db.ForeignKey('’'user.id’), nullable=False)# Lien vers l’utilisateur
 class FoundItem(db.Model):
 """Représente un objet retrouvé."""
 id = db.Column(db.Integer, primary_key=True)
 description = db.Column(db.String(200), nullable=False)
 date = db.Column(db.DateTime, default=datetime.utcnow)
 user_id = db.Column(db.Integer, db.ForeignKey(’user.id’), nullable=False ):