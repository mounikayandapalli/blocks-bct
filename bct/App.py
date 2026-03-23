from flask import Flask, render_template
from Blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    if len(blockchain.chain) == 1:
        transactions = [
            "Mounika sends 10 BTC to kalyani",
            "kalyani sends 5 BTC to greeshma",
            "greeshma sends 2 BTC to Meena",
            "Meena sends 1 BTC to dhana",
            "dhana sends 0.5 BTC to janu"
        ]

        for tx in transactions:
            previous_block = blockchain.get_previous_block()
            proof = blockchain.proof_of_work(previous_block['proof'])
            previous_hash = blockchain.hash(previous_block)
            blockchain.create_block(proof, previous_hash, tx)

    return render_template('index.html', chain=blockchain.chain)

if __name__ == '__main__':
    app.run(debug=True)