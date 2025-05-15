from flask import Flask, jsonify, request


app = Flask(__name__)

dados = []

@app.route('/request', methods=['POST'])
def receber_lista():
    global dados
    payload = request.get_json()

    if not payload or not isinstance(payload, list):
        return jsonify({"ERRO":'Erro'}), 400

    dados = payload

    return jsonify({'Mensagem': 'Lista recebedida', 'lista': len(dados)})

@app.route('/request',methods=['GET'])
def enviar_lista():
    global dados
    return jsonify(dados), 200

if __name__ == '__main__':
    app.run()
