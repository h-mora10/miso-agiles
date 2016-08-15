# -*- coding: utf-8 -*-
def fibonacci(numero):
    if numero <= 1:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

# Número que será el límite superior de la serie
numMax = int(raw_input("Ingrese hasta cuál número desea calcular la Serie de Fibonacci?: "))

# Ciclo que calcular la serie
resultado = []
numActual = 0
fibActual = fibonacci(numActual)
while fibActual < numMax:
    resultado.append(fibActual)
    numActual = numActual + 1
    fibActual = fibonacci(numActual)

# Impresión de la serie
print "Serie de Fibonacci: ", resultado