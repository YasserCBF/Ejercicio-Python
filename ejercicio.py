#algoritmo para detectar la palabra mas larga
print("La palabra más larga es:", max(input("Ingresa palabras: ").split(','), key=len))

#algoritmo de swecuencia de fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10)

#validacion de contraseña
import re
def validar_contraseña(c):
    return (6 <= len(c) <= 16 and 
            all(re.search(r, c) for r in [r'[a-z]', r'[A-Z]', r'[0-9]', r'[$#@]']))
print("Válida" if validar_contraseña(input("Ingrese su contraseña: ")) else "Inválida")

 