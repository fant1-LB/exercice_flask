from ..app import app
from flask import render_template
import requests
import json


@app.route("/")
def accueil():
    return "il faut mettre l'identifiant dans l'adresse!!"
@app.route("/retrievewikidata", defaults={'identifiant':None})
@app.route('/retrievewikidata/<identifiant>')
def requete(identifiant):
    r = requests.get (f'https://www.wikidata.org/wiki/Special:EntityData/{identifiant}.json')
    statut = r.status_code
    code = r.encoding
    data_json = r.text
    infos_type = r.json
  
    return render_template("wikidata.html", identifiant=identifiant, statut=statut, code = code, data_json=data_json, infos_type = infos_type)