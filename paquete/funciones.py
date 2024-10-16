def mostrar_filas_matriz(matriz:list) -> None:
    '''
    Muestra las filas de la matriz
    recibe list
    devuelve none
    '''
    if type(matriz) != list:
        print("El parametro debe ser una lista")
        return None
    
    for filas in matriz:
        print(filas)
        
def sumar_articulos_provincia(matriz:list , lista_depositos:list) -> list:
    '''
    Suma los articulos por provincia 
    recibe list, list
    devuelve list
    '''
    if type(matriz) != list:
        print("El parametro debe ser una lista")
        return None
    
    if type(lista_depositos) != list:
        print("El parametro debe ser una lista")
        return None

    matriz_total_articulos_deposito = []

    for provincia in lista_depositos:
        total_articulos = 0
        for i in range(len(matriz)):
            if matriz[i][0] == provincia:
                total_articulos += matriz[i][2]
        
        matriz_total_articulos_deposito +=[[provincia, total_articulos]]
        
    return matriz_total_articulos_deposito
    
def verificar_unidades_provincia(matriz:list, lista_depositos:list) -> list:
    '''
    verifica si hay algun articulo que tenga un stock mayor 
    a 3000000 unidades por provincia
    Recibe list, list
    Devuelve list
    '''
    if type(matriz) != list:
        print("El parametro debe ser una lista")
        return None
    
    if type(lista_depositos) != list:
        print("El parametro debe ser una lista")
        return None
        
    matriz_articulos_reponer_provincia = []
    
    for provincia in lista_depositos:
        for i in range(len(matriz)):
            if matriz[i][0] == provincia:
                if matriz[i][2] < 3000:
                    articulo_a_reponer = matriz[i][1]                         
                    matriz_articulos_reponer_provincia +=[[provincia, articulo_a_reponer]]
    
    return matriz_articulos_reponer_provincia

def verificar_articulos_provincia(matriz:list, lista_articulos:list) -> list:
    '''
    Verifica en que provincias se encuentra ese mismo tipo de articulo
    recibe list, list
    devuelve list
    '''
    if type(matriz) != list:
        print("El parametro debe ser una lista")
        return None
    
    if type(lista_articulos) != list:
        print("El parametro debe ser una lista")
        return None
    
    matriz_articulos_provincia = []
    for articulos in lista_articulos:
        provincia = []
        for i in range(len(matriz)):
            if matriz[i][1] == articulos and (matriz[i][2]) > 0 :
                provincia += [matriz[i][0]]                         
        matriz_articulos_provincia +=[[articulos, provincia]]
    
    return matriz_articulos_provincia

def cargar_aleatoriamente(matriz:list) -> list:
    '''
    Carga aleatoriamente corrigiendo errores lo que necesites dentro de la lista
    '''
    if type(matriz) != list:
        print("El parametro debe ser una lista")
        return None

    seguir = "s"

    while seguir == "s":
        fila = int(input("\nIngrese fila a corregir: "))
        while fila > (len(matriz) - 1): #Porque arranco en 0
            fila = int(input("ERROR.Ingrese fila a corregir: "))
            
        columna = int(input("Ingrese columna a corregir: "))
        while columna > (len(matriz[0]) - 1): #Porque arranco en 0
            columna = int(input("ERROR.Ingrese columna a corregir: "))
        
        if columna == 0:
            provincia =input("Ingrese valor a corregir: ")
            matriz[fila][columna] = provincia
        elif columna == 1:
            articulo =input("Ingrese valor a corregir: ")
            matriz[fila][columna] = articulo
        else:
            valor = int(input("Ingrese valor a corregir: "))
            matriz[fila][columna] = valor
            
        seguir = input("Desea cargar mas correciones s/n")
    
    return matriz

def sumar_total_articulos(matriz:list) -> list:
    '''
    Suma todos los articulos en todas las provincias
    '''
    if type(matriz) != list:
        print("El parametro debe ser una lista")
        return None
    
    total_articulos = 0
    for i in range(len(matriz)):
        total_articulos += matriz[i][2]

    return total_articulos

def suma_por_articulos_totales(matriz:list, lista_articulos:list) -> list:
    '''
    Suma el Total por articulo en todas las provincias
    
    '''
    if type(matriz) != list:
        print("El parametro debe ser una lista")
        return None
    
    if type(lista_articulos) != list:
        print("El parametro debe ser una lista")
        return None
    
    matriz_suma_articulos = []
    for articulos in lista_articulos:
        cantidad_total_articulos = 0
        for i in range(len(matriz)):
            if matriz[i][1] == articulos:
                cantidad_total_articulos += matriz[i][2]                       
        matriz_suma_articulos +=[[articulos, cantidad_total_articulos]]
    
    return matriz_suma_articulos

def calcular_porcentaje_articulo(matriz_suma_articulos:list, total_articulos:int)->list:
    '''
    Calcula el Porcentaje por articulo
    recibe list, list
    devuelve list
    '''
    if type(matriz_suma_articulos) != list:
        print("El parametro debe ser una lista")
        return None
    
    
    matriz_porcentaje_articulos = []
    
    for i in range(len(matriz_suma_articulos)):
        porcentaje_articulo = (100 * matriz_suma_articulos[i][1]) / total_articulos
        matriz_porcentaje_articulos +=[[matriz_suma_articulos[i][0],matriz_suma_articulos[i][1],
                                        porcentaje_articulo]]

    return matriz_porcentaje_articulos


#Ejercicio 8
# def calcular_recaudacion_deposito(matriz_ventas:list,lista_precios) -> list:

def ordenar_bubble(matriz_recaudacion:list) -> list:
    '''
    Ordena una lista
    Recibe list
    Devuelve list
    '''
    for i in range(len(matriz_recaudacion)):
        for j in range(len(matriz_recaudacion[i])):
            if matriz_recaudacion[j] > matriz_recaudacion[j+1]:
                aux = matriz_recaudacion[j]
                matriz_recaudacion[j] = matriz_recaudacion[j+1]
                matriz_recaudacion[j+1] = aux
    return matriz_recaudacion