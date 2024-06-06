frutas = []
TotalSalpicon = 0

cantidadDigitada = int(input("Ingrese la cantidad de frutas a usar: "))

for cont in range(1, cantidadDigitada + 1):
    print('---------Frutas & Salpicones-----------')

    fruta = {}
    fruta["id"] = input("ID: ")
    fruta["nombre"] = input("Nombre: ")
    fruta["precio"] = float(input("Precio: "))
    fruta["cantidad"] = int(input("Cantidad: "))

    TotalSalpicon += fruta["precio"] * fruta["cantidad"]

    frutas.append(fruta)

print()
print(f'Precio total del salpicón: {TotalSalpicon}$')
print()

frutas_ordenadas = sorted(frutas, key=lambda x: x["precio"], reverse=True)
print("Frutas ordenadas de mayor a menor según su precio:")
for fruta in frutas_ordenadas:
    print(f'{fruta["nombre"]}: ${fruta["precio"]}')


fruta_mas_barata = min(frutas, key=lambda x: x["precio"])
print(f'\nLa fruta más barata es: {fruta_mas_barata["nombre"]} (${fruta_mas_barata["precio"]})')