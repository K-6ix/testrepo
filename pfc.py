import random
choix=["pierre","feuille","ciseau"]
score_joueur=0
score_ordi=0  

def pfc(joueur, ordi):
    global score_joueur, score_ordi
    if joueur == ordi:
        print("vous avez le même choix")
        print("égalité")
    elif joueur == "pierre" and ordi == "feuille":
        score_ordi += 1
        print("vous avez perdu")
    elif joueur == "pierre" and ordi == "ciseau":
        score_joueur += 1
        print("vous avez gagné")
    elif joueur == "feuille" and ordi == "ciseau":
        score_ordi += 1
        print("vous avez perdu")
    elif joueur == "feuille" and ordi == "pierre":
        score_joueur += 1
        print("vous avez gagné")
    elif joueur == "ciseau" and ordi == "pierre":
        score_ordi += 1
        print("vous avez perdu")
    elif joueur == "ciseau" and ordi == "feuille":
        score_joueur += 1
        print("vous avez gagné")
while True: #demare une bcl inf tq break
    try:#indique le tes
        nb_manches = int(input("Combien de manches veux-tu jouer ? "))
        if nb_manches > 0:
            break#permet de sortir si c valide
        else:
            print("Le nombre de manches doit être supérieur à zéro.")
    except ValueError:#c lorsq qqchse!=int
        print("Tu dois entrer un nombre .")

for i in range(nb_manches):  # Tu peux changer le nombre de manches
    print(f"\nManche {i+1} sur {nb_manches}")
    joueur = input("Choisis: pierre, feuille ou ciseau ? ").lower()
    while joueur not in choix:
        print(" Mauvais choix. Tu dois choisir entre 'pierre', 'feuille' ou 'ciseau'.")
        joueur = input("Essaie encore : ").lower()

    ordi = random.choice(choix)
    print(f"L'ordinateur a choisi : {ordi}")
    pfc(joueur, ordi)

print("\nScore final :")
print("Joueur :", score_joueur)
print("Ordinateur :", score_ordi)

if score_joueur > score_ordi:
    print(" Tu as gagné la partie !")
elif score_joueur < score_ordi:
    print("L'ordinateur a gagné la partie.")
else:
    print("Match nul !")    


    