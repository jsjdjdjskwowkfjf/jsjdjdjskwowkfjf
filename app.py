from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "segredo"

produtos = [
    {"id":1,"nome":"Camiseta","preco":125},
    {"id":2,"nome":"Tênis Jordan","preco":1700},
    {"id":3,"nome":"Boné New Era","preco":160},
    {"id":4,"nome":"Óculos Travis Scott","preco":3000},
    {"id":5,"nome":"celular","preco":5000}
    {"id":6,"nome":"Moletom","preco":2000}
]

@app.route("/")
def index():
    return render_template("index.html", produtos=produtos)

@app.route("/add/<int:id>")
def add(id):
    if "carrinho" not in session:
        session["carrinho"] = []

    session["carrinho"].append(id)
    session.modified = True
    return redirect("/carrinho")

@app.route("/carrinho")
def carrinho():
    itens = [p for p in produtos if p["id"] in session.get("carrinho", [])]
    total = sum(p["preco"] for p in itens)
    return render_template("carrinho.html", itens=itens, total=total)

@app.route("/checkout", methods=["GET","POST"])
def checkout():

    if request.method == "POST":
        session["carrinho"] = []
        return render_template("checkout.html", mensagem="Compra realizada com sucesso!")

    return render_template("checkout.html", mensagem=None)
app.run(debug=True, host="0.0.0.0", port=5000)