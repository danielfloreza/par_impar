def verificar():
    number=int(input("Escriba un número: "))
    
    if number%2 !=0:
        print("El número "+str(number)+" es impar.\n")
    else:
        print("El número "+str(number)+" es par.\n")
    answer()


def answer():
    respuesta=int(input(""" Quieres continuar con el juego?
    
    1- Sí
    2- No
    
    """))
    
    if respuesta == 1:
        verificar()
    elif respuesta == 2:
        print("Nos vemos en la próxima!!\n")
    else:
        print("Escriba una opción válida.\n")
        answer()
    


def run():
    print("¡Bienvenido al juego PAR O IMPAR!\n")
    answer()


if __name__ == '__main__':
    run()