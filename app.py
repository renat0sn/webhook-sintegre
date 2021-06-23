from flask import Flask, request, Response, send_from_directory
from pathlib import Path
import requests
import wget

app = Flask(__name__)

@app.route('/')
def hello_world():
       return "Aplicação webhook funcionando!!!"

#caminho do webhook
@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json
 
    download_path = Path('download',data['nome'])
         
    resp=requests.get(data['url']).content
    with open("RDH.xlsx" , "wb") as arquivo_:
        arquivo_.write(resp)

    return Response(status=200)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
