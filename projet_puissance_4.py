def grille_vide():
    """créer la grille de depart"""
    return [[0 for _ in range(7)] for _ in range(6)]

def affiche(grille):
    """definit l'affichage la grille de jeu
        comme ceci :
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
    où . est une case vide, x le pion du joueur 1 et o le pion du joueur 2"""
    for ligne in grille:
        for element in ligne:
            if element == 0:
                print(" . ", end="")
            elif element == 1:
                print(" x ", end="")
            elif element == 2:
                print(" o ", end="")
        print()

def coup_possible(grille, col):
    """vérifie si un coup est possible dans la colonne donnée"""
    return grille[0][col] == 0


def jouer(grille, n_joueur, col):
    for ligne in reversed(grille):
        if ligne[col] == 0:
            ligne[col] = n_joueur
            break
    return grille
"""fonction qui place le pion du joueur dans la colonne choisie"""

def horizontal(grille, n_joueur, ligne, col):
    for i in range(0,3):
        if grille[ligne][col+i] != n_joueur:
            return False
    return True
"""fonction qui vérifie si il y a 4 pions alignés horizontalement, si c'est le cas elle renvoie true"""

def vertical(grille, n_joueur, lig, col):
    if lig > 2:
        return False
    for i in range(4):
        if grille[lig+i][col] != n_joueur:
            return False
    return True


"""si il y a 4 pions d'alignés dans une colonne alors c'est true"""

def diag_haut(grille, n_joueur, lig, col):
    for i in range(4):
        if grille[lig-i][col+i] != n_joueur:
            return False
    return True
"""si il y a 4 pions d'alignés en diagonale vers le haut alors c'est true"""

def diag_bas(grille, n_joueur, lig, col):
    for  i in range(4):
        if grille[lig+i][col+i] != n_joueur:
            return False
    return True
"""si il y a 4 pions d'alignés en diagonale vers le bas alors c'est true"""

def victoire(grille, n_joueur, lig, col):
    compteur = 0

    for i in range(lig, 6):      # de la ligne du pion vers le bas
        if grille[i][col] == joueur:
            compteur += 1
        else:
            break

    return compteur >= 4

"""Vérifie si une des conditions des focntions est respectée, si c'est le cas c'est gagné (true)"""

def match_nul(grille):
    for case in grille[0]:
        if case == 0 :
            return False
    return True
"""vérifie si il reste une case vide dans la grille, si c'est le cas ce n'est pas match nul (false) sinon c'est le cas donc true"""


grille = grille_vide() # initialisation de la grille
joueur = 1 # joueur 1 commence
fin = False 

while not fin: #boucle principale du jeu
    affiche(grille) # afficher la grille 

    col = int(input(f"Joueur {joueur}, choisis une colonne (0 à 6) : ")) # demander la colonne au joueur

    if col < 0 or col > 6: # vérifier que la colonne est valide
        print("Colonne invalide") #ecrit un message pour dire que la colonne est invalide
        continue 

    if not coup_possible(grille, col): # vérifier si le coup est possible
        print("Colonne pleine") # ecrit un message si la colonne est pleine
        continue 

    
    jouer(grille, joueur, col)# on joue le coup

    # chercher la ligne où le pion est tombé
    for lig in range(6): # parcourir les lignes
        if grille[lig][col] == joueur:  # si on trouve le pion du joueur
            ligne = lig # on garde la ligne
            break 

    # victoire ?
    if victoire(grille, joueur, ligne, col): # vérifier si le joueur a gagné
        affiche(grille) # afficher la grille
        print(f"🎉 Joueur {joueur} a gagné !") 
        fin = True

    # match nul ?
    elif match_nul(grille): # vérifier si c'est un match nul
        affiche(grille) # afficher la grille
        print("🤝 Match nul") 
        fin = True

    # changer de joueur
    else:
        joueur = 2 if joueur == 1 else 1 # changer de joueur