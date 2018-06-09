"""
Primero ejercicios en python.

Soluciones
"""
"""
Menu que lista todos los programas hechos en esta seccion.
"""


"""
Escribir un programa el cual encuentre todos los numeros 
divisibles entre 7 pero, que no son divisibles entre 5
entre 2000 y 3200.
"""
for i in range(2000,3200):
    if (i%5!=0) and (i%7==0):
        print i
"""
Escribir un programa que compute el factorial del numero
que el usuario desea saber,
"""
def factorial(n):
    if n > 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n -1)    
