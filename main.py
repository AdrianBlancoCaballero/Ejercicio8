# Ejercicio 8

import persistencia_json

lista = []

while True:
    marca = input("Marca de coche: ")
    if marca == "fin":
        break
    modelo = input("Modelo de coche: ")
    combustible = input("Tipo de combustible: ")
    cilindrada = input("Cilindrada del motor: ")

    datos = {}
    datos ["marca"] = marca
    datos ["modelo"] = modelo
    datos ["combustible"] = combustible
    datos ["cilindrada"] = cilindrada

    lista.append(datos)

persistencia_json.store(lista, "coches.txt")
lista = []
lista = persistencia_json.retrieve("coches.txt")

print("Lista de coches: \n", lista)