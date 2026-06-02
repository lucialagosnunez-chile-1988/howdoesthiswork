
inventario = ["espada", "antídoto", "poción"]
vida = 10

print("estás en el piso 1 de la mazmorra")
print("tu vida actual es:", vida)
print("tu inventario es")
print(inventario)

print("encuentras una poción")

respuesta = input("¿coger la poción? si/no: ")

if respuesta == "si":
    inventario.insert(0, "poción")
    print("tu inventario es")
    print(inventario)    

elif respuesta == "no":
    print("no cogiste la poción")

print("estás en el piso 1 de la mazmorra")

print("Encuentras un slime")
print("el slime te quita 3 de vida")
vida = vida - 3
print("tu vida actual es:", vida)

if "poción" in inventario:
    respuesta2 = input("Tienes una poción ¿deseas curarte?")
    if respuesta2 == "si":
        vida = vida + 3
        print("tu vida actual es:", vida)

else:
    print("estas en el piso 1")

print("estás en el piso 1 de la mazmorra")
