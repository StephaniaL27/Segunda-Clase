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