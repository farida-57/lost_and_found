## 📟 Lost & Found Flask App

### 📌 Description

**Lost & Found** est une application web développée avec **Flask** qui permet aux utilisateurs de déclarer et consulter des objets perdus ou retrouvés. Elle fournit une interface simple pour :

* S'enregistrer et se connecter
* Publier des annonces d’objets perdus ou retrouvés
* Associer un objet perdu à un objet retrouvé

---

### 📂 Structure du projet

```
lost_and_found/
├── .venv/                  # Environnement virtuel Python
├── instance/
│   └── database.db         # Base de données SQLite locale
├── static/                 # Fichiers statiques (CSS, JS, images, etc.)
├── templates/              # Templates HTML (Jinja2)
│   ├── base.html           # Template de base
│   ├── found.html          # Page des objets retrouvés
│   ├── home.html           # Page d’accueil
│   ├── login.html          # Connexion utilisateur
│   ├── lost.html           # Déclaration d’objet perdu
│   ├── match.html          # Association entre objets perdus et retrouvés
│   └── register.html       # Inscription utilisateur
├── .env                    # Variables d’environnement (non versionné)
├── .env.example            # Exemple de fichier `.env`
├── .gitignore              # Fichiers à ignorer par Git
├── app.py                  # Script principal de l'application Flask
├── get_secret_key.py       # Générateur de clé secrète
├── models.py               # Modèles de base de données SQLAlchemy
├── README.md               # (ce fichier)
└── requirements.txt        # Liste des dépendances Python
```

---

### ⚙️ Installation et configuration

#### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/lost_and_found.git
cd lost_and_found
```

#### 2. Créer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
.venv\Scripts\activate        # Windows
```

#### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

#### 4. Configurer la clé secrète

1. Crée un fichier `.env` à la racine :

   ```env
   SECRET_KEY=ta_clé_secrète_ici
   ```
2. Tu peux générer une clé avec :

   ```bash
   python get_secret_key.py
   ```

---

### 🚀 Lancer l'application

```bash
flask run
```

Accède à [http://127.0.0.1:5000](http://127.0.0.1:5000) dans ton navigateur.

---

### 🧐 Fonctionnalités principales

* 🔐 Authentification sécurisée
* 📄 Déclaration d’objets perdus
* 🔎 Affichage d’objets retrouvés
* 🔁 Matching entre objets perdus et retrouvés
* 🗃️ Stockage des données via SQLite et SQLAlchemy

---

### 📘 Technologies et Library utilisées

* [Flask](https://flask.palletsprojects.com/) pour la logique metier de lapplication
* [Jinja2](https://jinja.palletsprojects.com/) pour le templating avec HTML
* [SQLite](https://sqlite.org/) pour la base de donnees
* [SQLAlchemy](https://www.sqlalchemy.org/) pour communiquer avec la base de donnees
* [python-dotenv](https://pypi.org/project/python-dotenv/) pour charger les variables d'environnments

---

### ✅ À faire plutard

* [ ] Ajouter un système de messagerie entre utilisateurs
* [ ] Ajouter le support des images pour les objets
* [ ] Améliorer le style avec Bootstrap ou Tailwind CSS
* [ ] Déployer sur Render / Railway / Heroku




