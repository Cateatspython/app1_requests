#Importation des modules dotenv et os
import dotenv
import os

#Détermine le répertoire de base du projet avec BASE_DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.venv'))

#Création d'une classe Config()
class Config():
    DEBUG = os.environ.get("DEBUG")