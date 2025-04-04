import random

def generador(length):
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(length):
        password += random.choice(elements)
    print(f"Tu contraseña es: {password}")

