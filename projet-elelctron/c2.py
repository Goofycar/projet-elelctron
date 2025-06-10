from flask import Flask, request, render_template, redirect
import os
app = Flask(__name__, template_folder="templates", static_folder="static")
# Variables en mémoire
commande_actuelle = ""
dernier_resultat = ""

@app.route('/interface', methods=['GET', 'POST'])
def interface_web():
    global commande_actuelle, dernier_resultat
    if request.method == 'POST':
        commande_actuelle = request.form['commande']
        dernier_resultat = ""
        return redirect('/interface')
    return render_template("interface.html")

@app.route('/recuperer_commande', methods=['GET'])
def recuperer_commande():
    global commande_actuelle
    return commande_actuelle

@app.route('/get_resultat', methods=['GET'])
def get_resultat():
    global dernier_resultat
    return dernier_resultat

@app.route('/envoyer_resultat', methods=['POST'])
def recevoir_resultat():
    global dernier_resultat
    dernier_resultat = request.data.decode('utf-8', errors='replace')
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
