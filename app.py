# Importation des modules nécessaires
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from difflib import SequenceMatcher
from datetime import datetime
import os
from models import User, LostItem, FoundItem, db
from dotenv import load_dotenv


load_dotenv()

 # Création de l’application Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

 # Clé secrète pour sécuriser les sessions
basedir = os.path.abspath(os.path.dirname(__file__))

#Chemin de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'database.db')}"

# Désactiver les avertissements inutiles
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialisation de SQLAlchemy pour gérer la base dedonnées
db.init_app(app)

 # Créer les tables de la base de données
with app.app_context():
 db.create_all()

@app.route('/')
def home():
    """Affiche la page d'accueil avec tous les objets perdus et retrouvés."""
    lost_items = LostItem.query.all() # Récupère tous les objets perdus
    found_items = FoundItem.query.all() # Récupère tous les objets retrouvés
    return render_template('home.html', lost_items=lost_items,
    found_items=found_items)
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Permet à un utilisateur de s'inscrire."""
    if request.method == 'POST':
       username = request.form['username'] # Récupère le nom d’utilisateur du formulaire
       password = request.form['password'] # Récupère le mot de passe
       if not username or not password: 
           return render_template('register.html', error="Tous les champs sont requis")
       if User.query.filter_by(username=username).first():
        return render_template('register.html', error="Nom d’utilisateurdéjà pris")
       hashed_password = generate_password_hash(password,method='pbkdf2:sha256') # Hache le mot de passe
    
    
       user = User(username=username, password=hashed_password)    # Crée un nouvel utilisateur
       db.session.add(user) # Ajoute à la base de données
       db.session.commit() # Valide les changements
       return redirect(url_for('login')) # Redirige vers la page de connexion
    return render_template('register.html') # Affiche le formulaire d’inscription

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Permet à un utilisateur de se connecter."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first() # Cherche l’utilisateur
        if user and check_password_hash(user.password, password): # Vérifie le mot de passe
           session['user_id'] = user.id # Stocke l’ID utilisateur dans lasession
           session['username'] = user.username # Stocke le nom d’utilisateur
           return redirect(url_for('home')) # Redirige vers l’accueil
        return render_template('login.html', error="Identifiants incorrects")
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Déconnecte l'utilisateur."""
    session.pop('user_id', None) # Supprime l’ID utilisateur
    session.pop('username', None) # Supprime le nom d’utilisateur
    return redirect(url_for('home')) # Redirige vers l’accueil

@app.route('/lost', methods=['GET', 'POST'])
def lost():
    """Permet de déclarer un objet perdu."""
    if 'user_id' not in session:
        return redirect(url_for('login')) # Vérifie si l’utilisateur est connecté
    if request.method == 'POST':
        description = request.form['description']
        if not description:
           return render_template('lost.html', error="La description estrequise")
        lost_item = LostItem(description=description,user_id=session['user_id'])
        db.session.add(lost_item)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('lost.html')

@app.route('/found', methods=['GET', 'POST'])
def found():
    """Permet de déclarer un objet retrouvé."""
    if 'user_id' not in session:
       return redirect(url_for('login'))
    if request.method == 'POST':
        description = request.form['description']
        if not description:
           return render_template('found.html', error="La description estrequise")
        found_item = FoundItem(description=description,user_id=session['user_id'])
        db.session.add(found_item)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('found.html')

@app.route('/match')
def match():
    """Identifie les correspondances entre objets perdus et retrouvés."""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    lost_items = LostItem.query.all()
    found_items = FoundItem.query.all()
    matches = []
    for lost in lost_items:
       for found in found_items:
        similarity = SequenceMatcher(None, lost.description,found.description).ratio()
        if similarity > 0.6: # Seuil de similarité
            matches.append((lost, found, similarity))
    return render_template('match.html', matches=matches)
if __name__ == '__main__':
  app.run(debug=True) # Lance le serveur en mode débogage