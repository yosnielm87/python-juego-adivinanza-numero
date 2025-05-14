import logging
import random

# Para que los mensajes de logging.info() aparezcan en la consola,
# debes configurar el nivel de logging en INFO o más bajo (como DEBUG).
# Los niveles en orden ascendente son: DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def juego_adivinanza():
    # Generar un numero aleatorio del 1 al 100
    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinado = False

    logging.info("Bienvenido al juego de adivinanzas de numeros.")
    logging.info("Debes adivinar un numero del 1 al 10")
    logging.info("Intenta Adivinar!!!!!")

    while not adivinado:
        # Solicitar un numero
        numero = input(
            "Introduzca un numero del 1 al 100: "
        )  # el input siempre trabaja con string

        if numero.isdigit():
            numero = int(numero)  # Aqui se esta casteando de string a number
            intentos += 1

            if numero < numero_secreto:
                logging.warning(f"El numero secreto es mayor a {numero}")
                continue  # Pasa a la siguiente iteración del ciclo
            elif numero > numero_secreto:
                logging.warning(f"El numero secreto es menor a {numero}")
                continue  # Pasa a la siguiente iteración del ciclo
            else:
                logging.info(
                    f"¡FELICIDADES!!!! Has ganado!!!!!! El numero {numero} es el secreto...lo has logrado en {intentos} intentos"
                )
                adivinado = True  # Para salir del ciclo
        else:
            print("Por favor introduzca un numero")
            continue


if __name__ == "__main__":
    juego_adivinanza()
