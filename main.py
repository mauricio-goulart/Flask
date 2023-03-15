from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def ola():
    lista = ['Skyrim','Hogwarts Legacy','The Witcher 3']
    return render_template('index.html', titulo = 'Mauricio', jogos = lista)

app.run()

