# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getPokemonData
import os

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/pokemon', methods = ["GET", "POST"])
def pokemon():
    if request.method == "POST":
        poke_choice = request.form['poke_choice']
        data = getPokemonData(poke_choice)
        print(data)
        print("AYOOOOOOOOOOOOOOOOOOOOOO")
        return render_template("pokemon.html", time = datetime.now(), data = data)
    else:
        return "bro error you dummy dum."
