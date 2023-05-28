import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

# Em app encontra-se o nosso servidor web de Flask
app = Flask(__name__)
# Armazena a informação do PATH do projeto de acordo com o sistema utilizado
# diretorio_base = os.path.abspath(os.path.dirname(__file__))
# Insere o caminho correto na URI segundo o direório base
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(diretorio_base, 'database/database.db')

diretorio_base = os.path.abspath(os.path.dirname(__file__))
os.mkdir(os.path.join(diretorio_base, 'database'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(diretorio_base, 'database/database.db')

# Cursor para a base de dados SQLite
db = SQLAlchemy(app)


class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    diaria = db.Column(db.Float)
    combustivel = db.Column(db.String(20))
    lugares = db.Column(db.Integer)


with app.app_context():
    # Criação das tabelas
    db.create_all()
    # Execução das tarefas pendentes da base de dados
    db.session.commit()


@app.route('/')
def home():
    return 'Página inicial'


@app.route('/carros')
def listar_carros():
    carros = Carro.query.all()
    # Lógica para exibir a lista de carros


@app.route('/carros/<int:carro_id>')
def exibir_carro(carro_id):
    carro = Carro.query.get(carro_id)
    # Lógica para exibir os detalhes do carro


if __name__ == '__main__':
    app.run()
