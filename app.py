#Importation des fonctions de la bibliothèque Flask
from flask import Flask, render_template, jsonify
#Importation de la bibliothèque requests
import requests

#Initialisation d'une application Flask
app = Flask(__name__)

#Route pour la racine /
@app.route('/')
def home():
    return 'Page d\'accueil'

#Route pour retrieve_wikidata qui accepte les requêtes HTTP de type GET
@app.route('/retrieve_wikidata/<id>', methods=['GET'])
#Fonction qui sera exécutée quand on accède à la route /retrieve_wikidata/<id>
def retrieve_wikidata(id):
    wikidata_url = "https://www.wikidata.org/w/api.php"
    
    # Paramètres nécessaires pour interagir avec l'API de Wikidata
    params = {
        'action': 'wbgetentities',
        'ids': id,
        'format': 'json'
    }

    try:
        # Envoi de la requête à l'API Wikidata avec les paramètres spécifiés dans le dictionnaire params
        response = requests.get(wikidata_url, params=params)
        
        # Extraction des métadonnées de l'objet response renvoyé par la requête HTTP
        response_metadata = {
            "status_code": response.status_code,
            "content_type": response.headers.get("Content-Type", "Unknown")
        }

        # Vérification réussite de la requête effectuée avec requests.get()
        # Si c'est le cas conversion des données en format json 
        if response.status_code == 200:
            json_data = response.json()
            # Vérification de la présence des données de l'entité
            if 'entities' in json_data and id in json_data['entities']:
                entity_data = json_data['entities'][id]
            else:
                entity_data = None
        else:
            json_data = None
            entity_data = None

        # Retourner la page HTML avec les résultats
        return render_template(
            'wikidata.html',
            response_metadata=response_metadata,
            entity_data=entity_data
        )
    except Exception as e:
        # En cas d'erreur, retourner un message d'erreur JSON
        return jsonify({"error": str(e)}), 500

#Démarrer automatiquement quand exécution du script 
if __name__ == '__main__':
    app.run(debug=True)