#este programa es una torre de videojuego
#puedes subir pisos, bajarlos, volver al nivel 1
#el nivel 1 recupera tus fuerzas

#importando modulos
import sys
import time
import random

#definiendo variables
estado = 1
vida = 10

#bucle principal
#subir un piso es +1 a la variable estado
#bajar un piso es -1 a la variable estado

#hay un problema y es que la vida no tiene un máximo
#otro problema es que los enemigos son demasiado fuertes

#otro problema es que la vida al mínimo no te hace perder el juego

#no hay opciones como beber pociones

#al menos deberia tener mas pisos y mas pisos seguros entremedio

while True:
    while estado == 1:
        print("estás en el piso 1")
        print("todos tus puntos de vida han sido restaurados")
        vida = 10
        print("tu vida actual es: ", vida)
        respuesta = input("¿deseas subir al piso 2? subir/no ")
        if respuesta == "subir":
            estado = estado +1
        elif respuesta == "no":
            print("estás en el piso 1")
            print("tu vida actual es: ", vida)
            print("todos tus puntos de vida han sido restaurados")
            vida = 10
            
    while estado == 2:
        enemigo = random.randint(1,3)
        if enemigo == 1:
            print("¡Un slime te ataca!")
            vida = vida - 3

        elif enemigo == 2:
            print("¡Un esqueleto te ataca!")
            vida = vida - 4

        elif enemigo == 3:
            print("¡Un dragón pequeño te ataca!")
            vida = vida - 5
            
        print("Estás en el piso 2")
        print("tu vida actual es: ", vida)
        respuesta2 = input("¿Deseas subir o bajar?: subir/bajar ")
        if respuesta2 == "subir":
            estado = estado +1
        elif respuesta2 == "bajar":
            estado = 1
            
    while estado == 3:
        enemigo = random.randint(1,3)
        if enemigo == 1:
            print("¡Un slime te ataca!")
            vida = vida - 3

        elif enemigo == 2:
            print("¡Un esqueleto te ataca!")
            vida = vida - 4

        elif enemigo == 3:
            print("¡Un dragón pequeño te ataca!")
            vida = vida - 5
        print("Estás en el piso 3")
        print("tu vida actual es: ", vida)
        respuesta3 = input("¿Deseas subir, bajar o volver al primer piso?: subir/bajar/volver ")
        if respuesta3 == "subir":
            estado = estado +1
        elif respuesta3 == "bajar":
            estado = estado - 1
        elif respuesta3 == "volver":
            estado = 1
            
    while estado == 4:
        enemigo = random.randint(1,3)
        if enemigo == 1:
            print("¡Un slime te ataca!")
            vida = vida - 3

        elif enemigo == 2:
            print("¡Un esqueleto te ataca!")
            vida = vida - 4

        elif enemigo == 3:
            print("¡Un dragón pequeño te ataca!")
            vida = vida - 5

        print("tu vida actual es: ", vida)
        print("Estás en el piso 4")
            
        respuesta4 = input("¿Deseas subir, bajar o volver al primer piso?: subir/bajar/volver ")
        if respuesta4 == "subir":
            estado = estado +1
        elif respuesta4 == "bajar":
            estado = estado - 1.
        elif respuesta4 == "volver":
            estado = 1
            
    while estado == 5:
        print("encuentras poción")
        vida = 10
        print("tus puntos de vida están al máximo")
        print("tu vida actual es: ", vida)
        print("Estás en el piso 5")
        print("¡Felicitaciones, terminaste el juego!")
        print("The End")
        respuesta5 = input("¿Deseas jugar de nuevo? si/no ")
        if respuesta5 == "si":
            estado = 1
        if respuesta5 == "no":
            print("Gracias por jugar")
            time.sleep(10)
            sys.exit()
            
        


        
        
