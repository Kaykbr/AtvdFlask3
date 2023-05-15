from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/cartoes")
def cartoes():
    return render_template("paginas/cartoes.html", \
        titulo_pagina="Cartoes disponiveis")

@app.route("/cadastro")
def cadastro():
    return render_template("paginas/cadastro.html", \
        titulo_pagina="cadastro de cartoes")

@app.route("/pontos")
def pontos():
    return render_template("paginas/pontos.html", \
        titulo_pagina="pontos")

@app.route("/loja")
def loja():
    return render_template("paginas/loja.html", \
        titulo_pagina="loja")

if __name__ == "__main__":
    app.run(debug=True)