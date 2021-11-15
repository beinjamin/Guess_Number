import random
nombreMagique = random.randint(1, 26)

for i in range (0, 4):
    print("Testnummer", i+1)
    nombreEntre = input ("Hallo Sir, vielen Dank, dass Sie eine Zahl erraten haben::::...................")
    nombreEntre = int(nombreEntre)
    if nombreEntre > nombreMagique:

        print ("Ihre eingegebene Zahl ist größer als die magische Zahl !! Bitte geben Sie eine andere Zahl ein")

    if nombreEntre < nombreMagique:
        print("Ihre eingegebene Zahl ist der magischen Zahl unterlegen !!! Bitte geben Sie eine andere Zahl ein")

    if nombreEntre == nombreMagique:
        print("Gut gemacht, Sie haben die magische Zahl gefunden, die es tatsächlich ist ::::" , nombreMagique)

        break

else:
    print("egal, versuche es noch einmal, die magische Zahl lautete:::::"

 , nombreMagique)