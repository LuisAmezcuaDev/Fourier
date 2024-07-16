import math

m = float(input('ingresa el valor de m: '))
suma_resCos = 0
suma_resSin = 0

suma_resCos2 = 0
suma_resSin2 = 0

for i in range(5):
    coseno = math.cos((m * i * math.pi)/5)  # Calcula el coseno
    seno = -math.sin((m * i * math.pi)/5)
    
    resCos = ((0.2) * i) * coseno
    resSin = ((0.2) * i) * seno

    suma_resCos += resCos
    suma_resSin += resSin
    # Muestra el resultado por consola
    # print(f"Cos({i}) = {coseno} - Sin({i}) = {seno}")

    print(f"Cos({i}) = {round(resCos, 15)} y jSin({i}) = {round(resSin, 15)}j")

print(f":::::::::: La suma total de Cos es = {round(suma_resCos, 8)} :::::::::")
print(f":::::::::: La suma total de Sin es = {round(suma_resSin, 8)} :::::::::")

print(f'Para la funcion 2')

for i in range(5, 10):
    coseno = math.cos((m* i * math.pi)/5)  # Calcula el coseno
    seno = -math.sin((m * i * math.pi)/5)
    
    resCos = (((-0.2) * i)+2) * coseno
    resSin = (((-0.2) * i)+2) * seno

    suma_resCos2 += resCos
    suma_resSin2 += resSin
    # Muestra el resultado por consola
    # print(f"Cos({i}) = {coseno} - Sin({i}) = {round(seno, 15)}")
    print(f"Cos({i}) = {round(resCos, 15)} y jSin({i}) = {round(resSin, 15)}j")

print(f":::::::::: La suma total de Cos es = {round(suma_resCos2, 8)}")
print(f":::::::::: La suma total de Sin es = {round(suma_resSin2, 8)}")

sumaTCos = (suma_resCos + suma_resCos2)
sumaTSin = (suma_resSin + suma_resSin2)

print(f'::::::::::: El resultado es: {round(sumaTCos, 8)} y {round(sumaTSin, 8)}j :::::::::::::')