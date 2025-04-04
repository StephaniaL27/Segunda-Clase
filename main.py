import random

def lista():
    lista = []
    for i in range(3):
        a = input('¿Qué deseas agregar a la lista?')
        lista.append(a)
    print(lista)

def diccionario():
    diccionario = {}
    for i in range(3):
        a = input('¿Qué deseas agregar al diccionario?')
        b = input('¿Qué valor deseas agregar al diccionario?')
        diccionario[a] = b
    print(diccionario)

def generador(length):
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(length):
        password += random.choice(elements)
    print(f"Tu contraseña es: {password}")

length = int(input("¿Cuántos caracteres deseas que tenga tu contraseña?"))

generador(length)