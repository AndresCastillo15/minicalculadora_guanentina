# Menú de opciones
print("╔═══════════════════════════════════╗")
print("1 = Sumar (x + y)")
print("2 = Restar (x - y)")
print("3 = Multiplicar (x * y)")
print("4 = Dividir (x / y)")
print("5 = Potencia (x ^ y)")
print("6 = Logaritmo (log(X) base Y)")
print("╚═══════════════════════════════════╝")

opcion = input("Elige una opción (1-6): ")
opcion = int(opcion)

# Digitar numeros
print("╔═══════════════════════════════════╗")
x = input("Digite su número (X): ")
y = input("Digite su número (Y): ")
print("╚═══════════════════════════════════╝")

# convertir x/y en numero
x = float(x)
y = float(y)

# Procesar según la opción elegida
if opcion == 1:
    resultado = x + y
elif opcion == 2:
    resultado = x - y
elif opcion == 3:
    resultado = x * y
elif opcion == 4:
    if y != 0:
        resultado = x / y
    else:
        resultado = "Error: División por cero"
elif opcion == 5:
    resultado = x ** y 
elif opcion == 6:
    if x > 0 or y > 0:
        import math
        resultado = math.log(x, y)
    else:
        resultado = "Error: Logaritmo no válido (X y Y deben ser mayores que 0)"

else:
    print("No valido")

# Mostrar el resultado
print("╔═══════════════════════════════════╗")
print("Resultado:", resultado)
print("╚═══════════════════════════════════╝")
