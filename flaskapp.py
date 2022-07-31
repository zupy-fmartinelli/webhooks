from flask import json
from flask import request
from flask import Flask

import firebase_admin
from firebase_admin import credentials

# Importando o modulo do Firestore
from firebase_admin import firestore

# criando a api key e salvando
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# criar uma variave para associar ao banco de dados do firestore
db=firestore.client()


app = Flask(__name__)
@app.route('/')
def hello():
    return "Welcome to Flask Application!"

@app.route('/webhooks')
def zupyhooks():
      if request.headers['Content-Type'] == 'application/json':
        my_info = json.dumps(request.json)
        print(my_info)        
    #Salva o arquivo no Firebase no formato Json que retornou
        db.collection('zupyhooks').add(request.json)
    #retorna o token de autenticação
        return my_info



if __name__ == "__main__":
    app.run(host='0.0.0.0')
    