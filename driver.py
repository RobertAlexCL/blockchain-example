from flask import Flask, jsonify
from blockchain import Blockchain

'''
   Pequeña simulacipon de una blockchain utilizando Proof of Work
   referencia: https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
'''

app = Flask(__name__)
 
blockchain = Blockchain()
 
# Aquí se crea el endpoint para minar un nuevo bloque
@app.route('/minar', methods=['GET'])
def mineBlock():
    previusBlock = blockchain.returnPrevoiusBlock()
    prevoiusProof = previusBlock['proof']
    proof = blockchain.proofOfWork(prevoiusProof)
    previousHash = blockchain.hash(previusBlock)
    block = blockchain.addBlock(proof, previousHash)
     
    response = {'Mensaje': 'Bloque minado',
                'indice': block['index'],
                'Fecha': block['timestamp'],
                'Prueba': block['proof'],
                'Hash anterior': block['previous_hash']}
     
    return jsonify(response), 200
 
# Se verifica si la cadena de bloques es válida
@app.route('/validar', methods=['GET'])
def valid():
    valid = blockchain.checkChain(blockchain.chain)
     
    if valid:
        response = {'Mensaje': 'Blockchain válido.'}
    else:
        response = {'Mensaje': 'Blockchain no válido.'}
    return jsonify(response), 200
 
 
# Para ejecutar la web app de forma local
app.run(host='127.0.0.1', port=5000)