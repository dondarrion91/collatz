n = int(input("Ingrese n:"))
serie = n,
cantidad = 1
suma = n
may = None

def odd_collatz(n):
    return n // 2

def even_collatz(n):
    return 3*n + 1

while n != 1:
    if n % 2 == 0:
        n = odd_collatz(n)
        serie += n,
    elif n % 2 == 1:
        n = even_collatz(n)
        serie += n,

    if may is None or n > may:
        may = n

    suma += n
    cantidad += 1

promedio = round(suma / cantidad, 1)

print("n = ", n)
print("Orbita de n =", n, ": ", serie)
print("Longitud de la órbita (cantidad de valores calculados hasta llegar al 1): ", cantidad)
print("Promedio de todos los valores de la órbita:  ", promedio)
print("Mayor de los números en esa órbita: ", may)