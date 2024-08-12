# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Lista de temperaturas en grados Celsius
temperaturas_celsius = [0, 20, 100, -40]
# Usar map para convertir cada temperatura a Fahrenheit
temperaturas_fahrenheit = list(map(celsius_a_fahrenheit, temperaturas_celsius))
print(temperaturas_fahrenheit)
