from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity 

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Verify username and password (use a database in a real application)
    if username == 'admin' and password == 'admin123':
        access_token = create_access_token(identity={'role': 'admin'})
        return jsonify(access_token=access_token), 200
    elif username == 'user' and password == 'user123':
        access_token = create_access_token(identity={'role': 'core'})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run()
