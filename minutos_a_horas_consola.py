def convertir(min):
    horas = min // 60
    minutos = min % 60
    if minutos == 0:
        print(f"{min} Minutos = {horas} Horas")
    else:
        print(f"{min} Minutos = {round(min / 60, 2)} Horas y Minutos = {horas} Horas y {minutos} Minutos")

minutos = int(input('minutos: '))
convertir(minutos)