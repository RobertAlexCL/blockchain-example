import datetime
import hashlib
import json
 
class Blockchain:
    # Esta función nos crea el bloque génesis
    def __init__(self):
        self.chain = []
        self.addBlock(proof=1, previous_hash='0')
 
    # Esta función agrega más bloques a la cadena
    def addBlock(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
       
    # Esta función nos devuelve el bloque anterior
    def returnPrevoiusBlock(self):
        return self.chain[-1]
       
    # Esta función se encarga del proof of work
    def proofOfWork(self, previousProof):
        newProof = 1
        validProof = False
         
        while validProof is False:
            hash_operation = hashlib.sha256(
                str(newProof**2 - previousProof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                validProof = True
            else:
                newProof += 1
                 
        return newProof
 
    def hash(self, block):
        encryptedBlock = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encryptedBlock).hexdigest()
 
    def checkChain(self, chain):
        preoviusBlock = chain[0]
        indexBlock = 1
         
        while indexBlock < len(chain):
            block = chain[indexBlock]
            if block['previous_hash'] != self.hash(preoviusBlock):
                return False
               
            previousProof = preoviusBlock['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previousProof**2).encode()).hexdigest()
             
            if hash_operation[:5] != '00000':
                return False
            preoviusBlock = block
            indexBlock += 1
         
        return True
 