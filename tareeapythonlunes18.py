#este programa es una posada de videojuego

#darle la bienvenida al usuario
print("Bienvenido a la Posada del Aventurero!")

#preguntar al usuario su nombre
nombre = input("¿Cuál es tu nombre? ")

#ofrecerle un menu de comida al jugador
respuesta = input("¿Qué te vas a servir? tenemos: pescado frito/ lentejas/ pollo asado ")

#en caso de que la respuesta sea pescado frito
if respuesta == "pescado frito":
    print("Aquí tienes tu orden, ¡Buen provecho!")

#en caso de que la respuesta sea lentejas
elif respuesta == "lentejas":
    print("Aquí tienes tu orden, ¡Buen provecho!")

#en caso de que la respuesta sea pollo asado
elif respuesta == "pollo asado":
    print("Aquí tienes tu orden, ¡Buen provecho!")

#terminamos con el menu de comidas

#se le pregunta al jugador si quiere descansar a su pj en esta posada
respuesta2 = input("¿Deseas descansar en la posada? si/no ")

#en caso de que si
if respuesta2 == "si":
    print("has descansado en la posada del aventurero, vuelve pronto")

#en caso de que no
elif respuesta2 == "no":
    print("te has servido una comida en la posada del aventurero, vuelve pronto")
