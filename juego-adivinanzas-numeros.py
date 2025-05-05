
import random

def juego_adivinanza():
    # Generar un numero aleatorio del 1 al 100
    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanzas de numeros.")
    print("Debes adivinar un numero del 1 al 10")
    print("Intenta Adivinar!!!!!")

    while not adivinado:
        # Solicitar un numero
        numero = input("Introduzca un numero del 1 al 100: ")  # el input siempre trabaja con string

        if numero.isdigit():
            numero = int(numero)  # Aqui se esta casteando de string a number
            intentos += 1

            if numero < numero_secreto:
                print(f"El numero secreto es mayor a {numero}")
            elif numero > numero_secreto:
                print(f"El numero secreto es menor a {numero}")
            else:
                print(
                    f"¡FELICIDADES!!!! Has ganado!!!!!! El numero {numero} es el secreto...lo has logrado en {intentos} intentos"
                )
        else:
            print("Por favor introduzca un numero")

juego_adivinanza()
