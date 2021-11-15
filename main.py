import random
nombreMagique = random.randint(1, 26)

for i in range (0, 4):
    print("Essai Numero", i+1)
    nombreEntre = input ("Bonjour Monsieur Merci de deviner un nombre")
    nombreEntre = int(nombreEntre)
    if nombreEntre > nombreMagique:

        print ("Votre nombre que vous avez entrer est superieur au nombre magique")

    if nombreEntre < nombreMagique:
        print("Votre nombre que vous avez entrer est inferieux au nombre magique")

    if nombreEntre == nombreMagique:
        print("Bravo vous avez trouver le nombre magique il s'agit bien de " , nombreMagique)

        break

else:
    print("ce n'est pas grave , essayez encore uen fois ?? le nombre magique etait:" , nombreMagique)