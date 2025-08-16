#Adivina el numero

"""
crea un juego en el que la computadora elige un numero al azar entre 1 y 100 y el usuario tiene que adivinarlo, el programa debe dar pistas al usuario si su numero es mayor o menor que el numero secreto. El juego termina cuando el usuario adivina el numero
1. importa la libreria random
2. genera un numero aleatorio entre 1 y 100 y guardalo en una variable
3. inicia un bucle que se repita hasta que el usuario adivine el numero
4. dentro del bucle pide al usuario que ingrese un numero
5. compara el numero del usuario con el numero secreto y da una pista ('demasiado alto', 'demasiado bajo')
6. si el usuario adivina, imprime un mensaje de felicitacion y termina el bucle
"""
# importamos randit de la libreria random, para que python nos escoja un numero al azar
from random import randint

numero_secreto = randint(1, 100)

contador = 0

# comenzar con el bucle infinito

while contador < 5:
    numero = int(input("ingrese un numero entre 1 y 100: "))
    if 0 < numero <= 100:
        if numero == numero_secreto:
            print("Ganaste!, El numero que ingresaste es igual al numero secreto")
            break
        elif numero < numero_secreto:
            print("El numero que ingresaste es menor que el numero secreto")
            contador += 1
        elif numero > numero_secreto:
            print("El numero que ingresaste es mayor que el numero secreto")
            contador += 1
        else:
            print("ingrese un numero valido")
        print(f"van {contador} intentos, le quedan {5 - contador} intentos")
    else:
        print("debe ingresar un numero entre 1 y 100")
if contador == 5:
    print(f"se te acabon los intentos, suerte para la proxima")
     
