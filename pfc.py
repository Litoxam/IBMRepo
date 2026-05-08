#!/usr/bin/env python3

import random

print(f" --- BIENVENU AU TOURNOI PYTHON ---")

player = {"name": "me", "score": 0, "history":[]}
computer_score = 0
choices = ["pierre", "feuille", "ciseaux"]



print()
player["name"] = input('Entrez votre nom : ')

round = 1

while player["score"] < 3 and computer_score < 3:
    print("-" * 10 +  "Manche {}".format(round) + "-" * 10)

    user_choice = input("(pierre, feuille, ciseaux) ? Votre choix : ")

    if user_choice not in choices:
        print(f"Le choix n'est pas dans la liste ! Réessayez !")
        user_choice = input("(pierre, feuille, ciseaux) ? Votre choix : ")

    computer_choice = random.choice(["pierre", "feuille", "ciseaux"])
    print("L'ordinateur a choisi : {}".format(computer_choice))
    
    player["history"].append(user_choice)
    if user_choice == "ciseaux" and computer_choice == "ciseaux":
        print(f"Egalité ! ")
        print()
        round +=1
        continue
    if user_choice == computer_choice:
        print (f"Egalité !")
        print()
        round += 1
        continue

    if user_choice == "pierre" and computer_choice == "ciseaux":
        player["score"] += 1
        print("=> Gagné ! {} remporte la manche.".format(player["name"]))
        print()
    elif user_choice == "ciseaux" and computer_choice == "feuille":
        player["score"] += 1
        print("=> Gagné ! {} remporte la manche.".format(player["name"]))
        print()
    elif user_choice == "feuille" and computer_choice == "pierre":
        player["score"] += 1
        print("=> Gagné ! {} remporte la manche.".format(player["name"]))
        print()
    else:
        computer_score += 1
        print(f"Perdu ! L'ordinateur remporte la manche.")
        print()
    print()
    round += 1

distincts_choices = set(player["history"])

print(f"--- RESULTAT FINAL ---")
if player["score"] == 3:
    print("Vainqueur : {} ({} - {}) ".format(player["name"], player["score"], computer_score))
    print("Historique de vos coups : {} ".format(player["history"]))
    print("Coups distincts utilisés durant la partie : {}".format(distincts_choices))
else:
    print("Vainqueur : L'ordinateur ({} - {}) ".format(computer_score, player["score"]))
    print("Historique de vos coups : {} ".format(player["history"]))
    print("Coups distincts utilisés durant la partie : {}".format(distincts_choices))



    

