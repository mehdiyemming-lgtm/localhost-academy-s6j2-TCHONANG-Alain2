taches = ["Reviser Python", "Faire les exercices", "Lire le cours"]


# print("1.", taches[0])
# print("2.", taches[1])
# print("3.", taches[2])
# taches = ["Faire les courses", "Réviser Python", "Appeler le client"]

# taches = ["Faire les courses", "Réviser Python", "Appeler le client"]

# while True:
#     a = input("Numéro de la tâche : ")

#     try:
#         a = int(a)

#     except ValueError as error:
#         print(error)
#         print("Entrez un nombre entier")

#     else:
#         if 1 <= a <= len(taches):
#             print(taches[a - 1])
#             break  # on ne sort de la boucle qu'après un affichage valide
#         else:
#             print(f"Choisissez un nombre entre 1 et {len(taches)}")

#     finally:
#         print("Fin de la tentative.")


def verifier_priorite(valeur):
    if valeur == "basse" or valeur == "haute":
        return valeur
    else:
        raise ValueError("La priorite doit etre basse ou haute.")
    
    


def ajouter_tache(taches, titre, priorite):
    nouvelle_tache = {"titre": titre, "priorite": priorite}
    taches.append(nouvelle_tache)
    return taches