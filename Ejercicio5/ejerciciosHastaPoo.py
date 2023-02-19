# Ejercicio Ficheros 1
'''numero = int(input("Introduce un número entero entre 1 y 10: "))

if numero < 1 or numero > 10:
    print("El número debe estar entre 1 y 10")
else:
    
    nombre_fichero = f"tabla-{numero}.txt"
    
    with open(nombre_fichero, "w") as fichero:
       
        for i in range(1, 11):
            resultado = i * numero
            linea = f"{i} x {numero} = {resultado}\n"
            fichero.write(linea)
    
    print(f"La tabla de multiplicar de {numero} se ha guardado en el fichero {nombre_fichero}")'''

# Ejercicio Ficheros 2

numero = int(input("Introduce un número entero entre 1 y 10: "))

'''if numero < 1 or numero > 10:
    print("El número debe estar entre 1 y 10")
else:
    nombre_fichero = f"tabla-{numero}.txt"
    
    try:
        
        with open(nombre_fichero, "r") as fichero:
            print(f"Tabla de multiplicar de {numero}:")
            print(fichero.read())
    except FileNotFoundError:
        print(f"No se ha encontrado el fichero {nombre_fichero}")'''

#Ejercicio 1 Funciones y Módulos 

'''def mostrar_primer_y_ultimo(elementos):
    if len(elementos) > 0:
        primer_elemento = elementos[0]
        ultimo_elemento = elementos[-1]
        print(f"El primer elemento es {primer_elemento} y el último elemento es {ultimo_elemento}")
    else:
        print("La lista, tupla o cadena está vacía")

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (6, 7, 8, 9, 10)
mi_cadena = "Hola mundo"
mostrar_primer_y_ultimo(mi_lista)
mostrar_primer_y_ultimo(mi_tupla)
mostrar_primer_y_ultimo(mi_cadena)'''

#Ejercicio 2 Funciones y Módulos

'''def sumar_elementos(elementos):
    suma = 0
    for elemento in elementos:
        suma += elemento
    return suma

mi_lista = [1, 2, 3, 4, 5]
resultado = sumar_elementos(mi_lista)
print(f"La suma de los elementos de la lista es: {resultado}")'''

#Ejercicio 3 Funciones y Módulos

'''def sumar_varargs(*args):
    suma = 0
    for elemento in args:
        suma += elemento
    return suma

resultado = sumar_varargs(1, 2, 3, 4, 5)
print(f"La suma de los elementos es: {resultado}")

resultado = sumar_varargs(10, 20, 30)
print(f"La suma de los elementos es: {resultado}")

resultado = sumar_varargs(2.5, 3.7, 1.2)
print(f"La suma de los elementos es: {resultado}")'''











