
def mostrar_primero_y_ultimo(elementos):
    print(f"El primer elemento es: {elementos[0]}")
    print(f"El último elemento es: {elementos[-1]}")

def sumar_varargs(*args):
    suma = 0
    for elemento in args:
        suma += elemento
    return suma