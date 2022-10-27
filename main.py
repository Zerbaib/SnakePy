from tkinter import *
from random import *

game = Tk() # creation d'une fenetre avec tk
game.title("Snake game") # on met sont nom

hauteur = game.winfo_screenheight() # on recuperre les donner de l'ecran de l'utilisateur
largeur = game.winfo_screenwidth()
H = str(int(hauteur/1.1)) # on met les dimensions qui vas a la taille de l'ecran
L = str(int(largeur/2))
game.geometry(L + "x" + H + "+0+0") # on applique la taille

LPlateau = largeur /2 # on met les dimention du plateau
HPlateau = hauteur /1.2

Plateau = Canvas(game, width = LPlateau, height = HPlateau, bg = "pink") # on cree le canva pour le jeu
Plateau.pack(side="bottom") # on met ou demmare le canvas

Barre = Text(game, width = int(largeur /2), height = int(HPlateau / 10), bg = "light blue") # on cree un canva pour le score
Barre.pack(side="top") # on place le canva
Barre.insert(END, "score: 0\n") # on met le score de base

NombreDeCases= 75 # On défini le nombre de cases sur le plateau

LargeurCase = (LPlateau / NombreDeCases) # on met les largeur d'une case
HauteurCase = (HPlateau / NombreDeCases)

game.mainloop() # on laisse tourner la fenettre pour le jeux