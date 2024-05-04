from flask import Flask
from flask import request
from flask import render_template
import sqlite3
app = Flask(__name__)

# página index
@app.route("/")
def hello_world():
    return render_template("home.html")

# página cadastro do usuário
@app.route('/cadastro')
def index():
    return render_template('cadastro.html')

# pega os dados digitados pelo usuário.
@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']

# senha diferente exibi um erro ao usuário.
    if senha != confirmar_senha:
        return "As senhas não coincidem. Tente novamente."

    # conecta com SQLite usuario.
    conn = sqlite3.connect('usuario.db')
    cursor = conn.cursor()

    # Inserir dados na tabela SQLite usuario.
    cursor.execute('''INSERT INTO usuario (nome, email, telefone, senha)
                      VALUES (?, ?, ?, ?)''', (nome, email, telefone, senha))

    # fechar
    conn.commit()
    conn.close()

    return "Cadastro realizado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)