# Definir una función lambda que suma dos números
sum = lambda a, b: a + b
# Usar la función lambda
resultado = sum(5, 3)
print(resultado)


# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Usar lambda con filter para obtener solo los números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)


# Ordenar una lista de tuplas
# Lista de tuplas
puntos = [(1, 2), (3, 1), (5, 4), (2, 3)]
# Ordenar la lista por el segundo elemento de cada tupla usando lambda
puntos_ordenados = sorted(puntos, key=lambda x: x[1])
print(puntos_ordenados)


# Combinacion con map()
# Lista de números
numeros = [1, 2, 3, 4, 5]
# Usar lambda con map para elevar al cuadrado cada número
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)
