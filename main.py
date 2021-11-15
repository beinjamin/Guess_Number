import random
nombreMagique = random.randint(1, 50)

for i in range (0, 4):

    nombreEntre = input ("Bonjour Monsieur Merci de deviner un nombre")


    if nombreEntre > nombreMagique:

        print ("Votre nombre que vous avez entrer est superieur au nombre magique")

    if nombreEntre < nombreMagique:
        print("Votre nombre que vous avez entrer est inferieux au nombre magique")