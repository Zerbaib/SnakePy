from tkinter import *
from random import *

game = Tk() # creation d'une fenetre avec tk
game.title("Snake game") # on met sont nom

hauteur = game.winfo_screenheight() # on recuperre les donner de l'ecran de l'utilisateur
largeur = game.winfo_screenwidth()
H = str(int(hauteur/1.1)) # on met les dimensions qui vas a la taille de l'ecran
L = str(int(largeur/2))
game.geometry(L + "x" + H + "+0+0") # on applique la taille

game.mainloop() # on laisse tourner la fenettre pour le jeux