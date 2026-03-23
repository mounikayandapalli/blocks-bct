#Simple Blockchain Web App (Flask)

This project is a basic implementation of a Blockchain system with a web interface built using Flask. It demonstrates how blocks are created, linked, and displayed with simple transaction data.

# Features
Custom Blockchain implementation
Proof of Work algorithm
SHA-256 hashing for block security
Simple transaction simulation
Web interface to visualize blocks
Genesis block creation

 #Technologies Used
Python
Flask
HTML (Jinja2 Template)
Hashlib (for SHA-256)

# How It Works
The application starts with a Genesis Block.
Predefined transactions are added automatically.

#Each block contains:
Index
Timestamp
Transaction data
Proof (from Proof of Work)
Previous block hash
Blocks are linked together using hashes, forming a chain.
The web page displays all blocks in a structured format.

#How to Run the Project
Step 1: Install dependencies
pip install flask
Step 2: Run the application
python App.py
Step 3: Open in browser
http://127.0.0.1:5000/

#Output
The web page will display a list of blocks like:
Block number
Timestamp
Transaction
Proof
Previous Hash

# Future Improvements
Add user input for transactions
Implement real-time mining
Add blockchain validation
Improve UI design
Store blockchain data permanently

#Author
Mounika Yandapalli
