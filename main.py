from paquete import *

lista_depositos = ["PBA","Jujuy","Neuquen"]
lista_articulos = ["quimicos","trapos","escobas","cepillos","papel higienico",
                   "jabon","pañuelos descartables"]

# 1. Obtener existencias: para ello deberá cargar en el main la existencia de 
# cada artículo en todos los depósitos. En una lista de cantidad, no uno por uno.
# Por lo que habrá una matriz con 3 columnas o filas, 
# provincia, tipo de artículo y cantidad.

lista_cantidad = [0] * len(lista_articulos)
matriz = []

for i in range(len(lista_depositos)):
    provincia = lista_depositos[i]
    print(f"En {provincia}:")
    for i in range(len(lista_articulos)):
        lista_cantidad[i] = int(input(f"Ingrese la cantidad de {lista_articulos[i]}: "))
        matriz += [[provincia, lista_articulos[i], lista_cantidad[i]]]

#resultados 1
print("\nMatriz Cargada ")
mostrar_filas_matriz(matriz)


# 2. Calcular por cada depósito la cantidad total de artículos almacenados entre 
# todos los tipos.

matriz_total_articulos_deposito = sumar_articulos_provincia(matriz,lista_depositos)

# resultados 2
print("\nMatriz con total articulos y provincia")
mostrar_filas_matriz(matriz_total_articulos_deposito)

    
# 3. Obtener los nombres de los artículos que es necesario reponer en cada depósito.
# Crear una función que devuelva todos los juguetes con menos de 3000 unidades.

matriz_articulos_a_reponer = verificar_unidades_provincia(matriz, lista_depositos)

# resultados 3
print("\nMatriz con tipos de articulos a reponer por deposito")
mostrar_filas_matriz(matriz_articulos_a_reponer)

# 4. Máxima cantidad de artículos almacenados de cada tipo. Devolver en qué 
# provincia se encuentran por si es necesario redistribuir.
matriz_articulos_provincia = verificar_articulos_provincia(matriz, lista_articulos)

# resultados 4
print("\nMatriz con tipos de articulos y donde se encuentran")
mostrar_filas_matriz(matriz_articulos_provincia)

# 5. Generar una función que permita corregir un error de carga mediante 
# carga aleatoria o distribuida de matrices.

matriz_corregida = cargar_aleatoriamente(matriz)

# resultados 5
print("\nMatriz corregida")
mostrar_filas_matriz(matriz_corregida)

# 6. Cantidad de depósitos que hayan almacenado más de 3.000.000 de unidades entre
# los 7 artículos. Mostrar provincias.

#USO LA MATRIZ CREADA EN EL PUNTO 2
print("\nResultados depositos con mas de 3000000")

cantidad_depositos_mayor = 0

for i in range(len(matriz_total_articulos_deposito)):
    provincia = matriz_total_articulos_deposito[i][0]
    cantidad = matriz_total_articulos_deposito[i][1]
    
    if matriz_total_articulos_deposito[i][1] > 3000000:
        cantidad_depositos_mayor += 1 
        print(f"Hay {cantidad} en {provincia} ")
    else:
        print(f"En {provincia} solo hay {cantidad}")
        
print(f"Hay {cantidad_depositos_mayor} depositos con mas de 3.000.000 de unidades")

# 7. Porcentaje de artículos de cada tipo sobre el total de artículos almacenados. 
# Realizar una función que muestre el porcentaje de cada uno.

total_articulos = sumar_total_articulos(matriz)

matriz_suma_por_articulo = suma_por_articulos_totales(matriz,lista_articulos)

matriz_porcentaje_articulo = calcular_porcentaje_articulo(matriz_suma_por_articulo, 
                                                          total_articulos)

# resultados 7
print("\nMatriz Porcentaje de artículos de cada tipo")
mostrar_filas_matriz(matriz_porcentaje_articulo)

# 8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor
# usando bubble sort o selection sort. Justificar la elección del algoritmo. 
# Para ello la función deberá recibir una matriz de ventas, y una lista de precios.

#ESTA EN LA PARTE DE FUNCIONES