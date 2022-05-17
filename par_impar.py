def verificar():
    number=input("Escriba un numero: ")
    
    number=number.strip()
    number=number.replace(" ", "")
    
    if number.isdigit():
        
        if int(number)%2 !=0:
            print("El numero "+str(number)+" es impar.\n")
        else:
            print("El numero "+str(number)+" es par.\n")
        answer()
    else:
        print("Escribe un número valido, sin letras ni puntos ni guiones.\n")
        verificar()


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
    print("Â¡Bienvenido al juego PAR O IMPAR!\n")
    answer()


if __name__ == '__main__':
    run()