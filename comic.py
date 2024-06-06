import random;


A = []
B = []
C = []
D = []
producto={}

TodasLasZonas = []
ids_utilizados = []

opcion = 0
TotalZonaA = 0
TotalZonaB = 0
TotalZonaC = 0
TotalZonaD = 0

while opcion != 5:
    print('****Korka Comics*****')
    print('1. Registrar producto')
    print('2. Ver inventario')
    print('3. Buscar producto')
    print('4. Editar producto')
    print('5. Salir')
    opcion = int(input('Digita una opción: '))

    if opcion == 1:
        producto = {}

        producto_id = random.randint(1, 100)

        AgregadoConExito=False

        while AgregadoConExito != True:

            if producto_id not in ids_utilizados:
                ids_utilizados.append(producto_id)

            producto["id"] = producto_id
            producto["nombre"] = input("Nombre: ")
            producto["precio"] = float(input("Precio: "))
            producto["zona"] = input("Zona: ").upper()
            producto["descripcion"] = input("Descripción: ")
            producto["referencia"] = input("Referencia: ")
            producto["casa"] = input("Casa a la que pertenece: ")
            producto["pais"] = input("País: ")
            producto["unidadesCompradas"] = int(input("Unidades compradas: "))

            if producto["precio"] > 500:
                producto["garantia"] = True
            else:
                producto["garantia"] = False


            if producto["zona"] == 'A':
                TotalZonaA += producto["unidadesCompradas"]
            elif producto["zona"] == 'B':
                TotalZonaB += producto["unidadesCompradas"]
            elif producto["zona"] == 'C':
                TotalZonaC += producto["unidadesCompradas"]
            elif producto["zona"] == 'D':
                TotalZonaD += producto["unidadesCompradas"]
            else:
                print('Zona ingresada no valida')
                break

            if TotalZonaA <= 50 and producto["zona"] == 'A':
                A.append(producto)
                TodasLasZonas.append(producto)
                print(f'Espacios disponibles en la zona A: {50 - TotalZonaA}')
                AgregadoConExito = True

            elif TotalZonaB <= 50 and producto["zona"] == 'B':
                B.append(producto)
                TodasLasZonas.append(producto)
                print(f'Espacios disponibles en la zona B: {50 - TotalZonaB}')
                AgregadoConExito = True

            elif TotalZonaC <= 50 and producto["zona"] == 'C':
                C.append(producto)
                TodasLasZonas.append(producto)
                print(f'Espacios disponibles en la zona C: {50 - TotalZonaC}')
                AgregadoConExito = True
                

            elif TotalZonaD <= 50 and producto["zona"] == 'D':
                D.append(producto)
                TodasLasZonas.append(producto)
                print(f'Espacios disponibles en la zona D: {50 - TotalZonaD}')
                AgregadoConExito = True
                
            else:
                print(f'Sin espacio en esta Zona !')
                break


    elif opcion == 2:
        for objeto in TodasLasZonas:
            print()
            print(f"ID: {objeto['id']}")
            print(f"Nombre: {objeto['nombre']}")
            print(f"Precio: {objeto['precio']}")
            print(f"Zona: {objeto['zona']}")
            print(f"Descripción: {objeto['descripcion']}")
            print(f"Referencia: {objeto['referencia']}")
            print(f"Casa: {objeto['casa']}")
            print(f"País: {objeto['pais']}")
            print(f"Unidades compradas: {objeto['unidadesCompradas']}")
            print(f"Garantía: {'Sí' if objeto['garantia'] else 'No'}")
            print("-" * 20)  # Separador para mejorar la visualización
    elif opcion == 3:
        userInput = input('Filtra por nombre: ')
        banda_encontrada = False 
        for producto in TodasLasZonas:
            if userInput == producto["nombre"]:
                print('Producto encontrado:')
                print(f'ID: {producto_id}')
                print(f'Nombre: {producto["nombre"]}')
                print(f'precio: {producto["precio"]}')
                print(f'descripcion: {producto["descripcion"]}')
                producto_encontrado = True
                break
    elif opcion == 4:
        userInput = input('Filtra por nombre: ')
        producto_encontrado = False 
        for producto in TodasLasZonas:
            if userInput == producto["nombre"]:
                print('Producto encontrado !')
                UnidadesDelProducto = producto["unidadesCompradas"]
                unidadIngresada = int(input("Ingrese nueva cantidad:"))
                if unidadIngresada <= UnidadesDelProducto:
                    producto["unidadesCompradas"] = unidadIngresada
                    producto_encontrado = True
                    print('producto editado con exito !')
                    break
                else:
                    print('La cantidad ingresada no puede ser mayor a la actual')
            else:
                print('Producto no encontrado !')
    elif opcion == 5:
            print("Finalizar")
    else:
         print("Opcion invalidad")
