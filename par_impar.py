def verificar():
    number=int(input("Escriba un número: "))
    
    if number%2 !=0:
        print("El numero "+str(number)+" es impar.\n")
    else:
        print("El numero "+str(number)+" es par.\n")
    answer()


def answer():
    respuesta=input(""" Quieres continuar con el juego?
    
    1- Si
    2- No
    
    """)
    respuesta=respuesta.replace(" ","")
    if respuesta.isdigit():
        
        if int(respuesta) == 1:
            verificar()
        elif int(respuesta) == 2:
            print("Nos vemos en la proxima!!\n")
        else:
            print("Escriba una opcion valida.\n")
            answer()
    else:
        print("Escriba una opcion valida.\n")
        answer()
    


def run():
    print("¡Bienvenido al juego PAR O IMPAR!\n")
    answer()


if __name__ == '__main__':
    run()