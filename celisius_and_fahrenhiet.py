def celisius_to_fahrenhiet(celisius):
    fahrenhiet = (celisius * 9/5 +32)
    print(fahrenhiet)

def fahrenhiet_to_celisius(fahrenhiet):
    celisius = (fahrenhiet - 32) * 5/9
    print(celisius)
def main():
    choix = 0
    while choix != 3:
        print("=== Menu de conversion de Temperateure ===")
        print("1. Convertir Celsius en fahrenhiet")
        print("2. Convertir fahrenhiet en Celsius")
        print("3. Quitter")
        choix = int(input("Entrer votre choix: "))

        if choix == 1:
            t = int(input("Entrer la temperateure en celsius: "))
            celisius_to_fahrenhiet(t)

        if choix == 2:
            t = int(input("Entrer la temperateure en fahrenhiet: "))
            fahrenhiet_to_celisius(t)

        if choix == 3:
            quit()


main()