from flask import Flask,render_template

class Jogos():
    def __init__(self, nome, tipo, console):
        self.nome = nome
        self.tipo = tipo
        self.console = console


app = Flask(__name__)


@app.route('/')
def Flask():
    jogo1 = Jogos('Skyrim', 'Rpg','Multiplataforma')
    jogo2 = Jogos('Pokemon X','Rpg','Nintendo 3DS')
    lista = [jogo1,jogo2]
    return render_template('index.html', titulo = 'Mauricio', jogos = lista)

app.run()

