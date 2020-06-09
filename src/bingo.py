# Los ceros representan celdas vacías
# Los unos representan celdas ocupadas

def carton():
    carton = (
        (1,0,1,0,1,0,1,0,1),
        (0,1,0,1,1,0,0,1,1),
        (1,1,0,1,0,1,0,1,0)
    )
    return carton

def no_menos_15(carton):
    cont = 0
    for fila in carton:
        for celda in fila:
            cont += celda
    return cont

def no_mas_15(carton):
    cont = 0
    for fila in carton:
        for celda in fila:
            cont += celda
    return cont

def elementos_columnas(carton):
    cont = 0
    for i in range(9):
        if(carton[0][i] == 1 or carton[1][i] == 1 or carton[2][i] == 1):
            cont += 1
    return cont

def elementos_filas(carton):
    cont = 0
    for i in range(3):
        for j in range(9):
            if carton[i][j] == 1:
                cont += 1
                break
    return cont