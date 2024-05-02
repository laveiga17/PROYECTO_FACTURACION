# Importaciones necesarias
import os
import time
from functools import reduce
from components import Menu, Valida
from utilities import borrarPantalla, gotoxy, reset_color, red_color, green_color, yellow_color, blue_color, purple_color, cyan_color
from clsJson import JsonFile
from company import Company
from customer import RegularClient
from sales import Sale
from product import Product
from iCrud import ICrud
import datetime

# Obtener la ruta del archivo actual
path, _ = os.path.split(os.path.abspath(__file__))

# Definición de la clase CrudClients
class CrudClients(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*39 + "Registro de Cliente" + " "*39 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Obtener los datos del cliente
        gotoxy(10, 5)
        nombre = input("Nombre del cliente: ")

        gotoxy(10, 6)
        apellido = input("Apellido del cliente: ")

        gotoxy(10, 7)
        cedula = validar.solo_numeros("Cédula del cliente (10 dígitos): ", 10, 7)

        # Validar la cédula ecuatoriana
        while len(cedula) != 10:
            gotoxy(10, 7)
            print("Cédula incorrecta. Deben ser 10 dígitos.")
            cedula = validar.solo_numeros("Cédula del cliente (10 dígitos): ", 10, 7)

        # Guardar el cliente en el archivo JSON
        nuevo_cliente = {
            "nombre": nombre,
            "apellido": apellido,
            "cedula": cedula
        }
        json_file = JsonFile(path+'/archivos/clients.json')
        clientes = json_file.read()
        clientes.append(nuevo_cliente)
        json_file.save(clientes)
        gotoxy(10, 10)
        print("Cliente registrado exitosamente.")
        input("Presione una tecla para continuar...")

    def update(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*38 + "Actualizar Cliente" + " "*38 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Obtener la cédula del cliente a actualizar
        gotoxy(10, 5)
        cedula = validar.solo_numeros("Ingrese la cédula del cliente a actualizar (10 dígitos): ", 10, 5)

        # Buscar el cliente por cédula en el archivo JSON
        json_file = JsonFile(path+'/archivos/clients.json')
        clientes = json_file.read()
        cliente_encontrado = None
        for cliente in clientes:
            if cliente["cedula"] == cedula:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            # Mostrar los datos actuales del cliente
            gotoxy(10, 7)
            print(f"Nombre actual: {cliente_encontrado['nombre']}")
            gotoxy(10, 8)
            print(f"Apellido actual: {cliente_encontrado['apellido']}")

            # Obtener los nuevos datos del cliente
            gotoxy(10, 10)
            nuevo_nombre = input("Nuevo nombre del cliente (deje en blanco para mantener): ")
            if nuevo_nombre:
                cliente_encontrado['nombre'] = nuevo_nombre

            gotoxy(10, 11)
            nuevo_apellido = input("Nuevo apellido del cliente (deje en blanco para mantener): ")
            if nuevo_apellido:
                cliente_encontrado['apellido'] = nuevo_apellido

            # Guardar los cambios en el archivo JSON
            json_file.save(clientes)
            gotoxy(10, 13)
            print("Cliente actualizado exitosamente.")
        else:
            gotoxy(10, 7)
            print("Cliente no encontrado.")
        input("Presione una tecla para continuar...")

    def delete(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*38 + "Eliminar Cliente" + " "*38 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Obtener la cédula del cliente a eliminar
        gotoxy(10, 5)
        cedula = validar.solo_numeros("Ingrese la cédula del cliente a eliminar (10 dígitos): ", 10, 5)

        # Buscar el cliente por cédula en el archivo JSON
        json_file = JsonFile(path+'/archivos/clients.json')
        clientes = json_file.read()
        cliente_encontrado = None
        for cliente in clientes:
            if cliente["cedula"] == cedula:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            # Mostrar los datos del cliente antes de eliminarlo
            gotoxy(10, 7)
            print(f"Nombre: {cliente_encontrado['nombre']}")
            gotoxy(10, 8)
            print(f"Apellido: {cliente_encontrado['apellido']}")
            gotoxy(10, 9)
            print("¿Está seguro que desea eliminar este cliente?")
            confirmacion = input("Ingrese 's' para confirmar, cualquier otra tecla para cancelar: ")

            if confirmacion.lower() == 's':
                clientes.remove(cliente_encontrado)
                json_file.save(clientes)
                gotoxy(10, 11)
                print("Cliente eliminado exitosamente.")
            else:
                gotoxy(10, 11)
                print("Eliminación cancelada.")
        else:
            gotoxy(10, 7)
            print("Cliente no encontrado.")
        input("Presione una tecla para continuar...")

    def consult(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*38 + "Consultar Clientes" + " "*38 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Leer los clientes desde el archivo JSON
        json_file = JsonFile(path+'/archivos/clients.json')
        clientes = json_file.read()

        # Mostrar la lista de clientes
        gotoxy(10, 5)
        print("Lista de Clientes:")
        gotoxy(10, 7)
        print("Nombre\t\tApellido\t\tCédula")
        line = 9
        for cliente in clientes:
            gotoxy(10, line)
            print(f"{cliente['nombre']}\t\t{cliente['apellido']}\t\t{cliente['cedula']}")
            line += 1

        input("Presione una tecla para continuar...")

# En la clase CrudProducts

class CrudProducts(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*39 + "Registro de Producto" + " "*39 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Obtener los datos del producto
        gotoxy(10, 5)
        descripcion = input("Descripción del producto: ")

        gotoxy(10, 6)
        precio = validar.solo_numeros("Precio del producto: ", 10, 6)

        gotoxy(10, 7)
        stock = validar.solo_numeros("Stock del producto: ", 10, 7)

        # Guardar el producto en el archivo JSON
        nuevo_producto = {
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock
        }
        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        productos.append(nuevo_producto)
        json_file.save(productos)
        gotoxy(10, 10)
        print("Producto registrado exitosamente.")
        input("Presione una tecla para continuar...")

    def update(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*38 + "Actualizar Producto" + " "*38 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Obtener la descripción del producto a actualizar
        gotoxy(10, 5)
        descripcion = input("Ingrese la descripción del producto a actualizar: ")

        # Buscar el producto por descripción en el archivo JSON
        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        producto_encontrado = None
        for producto in productos:
            if producto["descripcion"].lower() == descripcion.lower():
                producto_encontrado = producto
                break

        if producto_encontrado:
            # Mostrar los datos actuales del producto
            gotoxy(10, 7)
            print(f"Descripción actual: {producto_encontrado['descripcion']}")
            gotoxy(10, 8)
            print(f"Precio actual: {producto_encontrado['precio']}")
            gotoxy(10, 9)
            print(f"Stock actual: {producto_encontrado['stock']}")

            # Obtener los nuevos datos del producto
            gotoxy(10, 11)
            nuevo_descripcion = input("Nueva descripción del producto (deje en blanco para mantener): ")
            if nuevo_descripcion:
                producto_encontrado['descripcion'] = nuevo_descripcion

            gotoxy(10, 12)
            nuevo_precio = validar.solo_numeros("Nuevo precio del producto (deje en blanco para mantener): ", 10, 12)
            if nuevo_precio:
                producto_encontrado['precio'] = nuevo_precio

            gotoxy(10, 13)
            nuevo_stock = validar.solo_numeros("Nuevo stock del producto (deje en blanco para mantener): ", 10, 13)
            if nuevo_stock:
                producto_encontrado['stock'] = nuevo_stock

            # Guardar los cambios en el archivo JSON
            json_file.save(productos)
            gotoxy(10, 15)
            print("Producto actualizado exitosamente.")
        else:
            gotoxy(10, 7)
            print("Producto no encontrado.")
        input("Presione una tecla para continuar...")

    def delete(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*38 + "Eliminar Producto" + " "*38 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Obtener la descripción del producto a eliminar
        gotoxy(10, 5)
        descripcion = input("Ingrese la descripción del producto a eliminar: ")

        # Buscar el producto por descripción en el archivo JSON
        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        producto_encontrado = None
        for producto in productos:
            if producto["descripcion"].lower() == descripcion.lower():
                producto_encontrado = producto
                break

        if producto_encontrado:
            # Mostrar los datos del producto antes de eliminarlo
            gotoxy(10, 7)
            print(f"Descripción: {producto_encontrado['descripcion']}")
            gotoxy(10, 8)
            print(f"Precio: {producto_encontrado['precio']}")
            gotoxy(10, 9)
            print(f"Stock: {producto_encontrado['stock']}")
            gotoxy(10, 10)
            print("¿Está seguro que desea eliminar este producto?")
            confirmacion = input("Ingrese 's' para confirmar, cualquier otra tecla para cancelar: ")

            if confirmacion.lower() == 's':
                productos.remove(producto_encontrado)
                json_file.save(productos)
                gotoxy(10, 12)
                print("Producto eliminado exitosamente.")
            else:
                gotoxy(10, 12)
                print("Eliminación cancelada.")
        else:
            gotoxy(10, 7)
            print("Producto no encontrado.")
        input("Presione una tecla para continuar...")

    # En la clase CrudProducts

    def consult(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*38 + "Consultar Productos" + " "*38 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Leer los productos desde el archivo JSON
        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()

        # Mostrar la lista de productos
        gotoxy(10, 5)
        print("Lista de Productos:")
        gotoxy(10, 7)
        print("Descripción\t\tPrecio\t\tStock")
        line = 9
        for producto in productos:
            gotoxy(10, line)
            print(f"{producto['descripcion']}\t\t{producto['precio']}\t\t{producto['stock']}")
            line += 1

        input("Presione una tecla para continuar...")

    # En la clase CrudSales

class CrudSales(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*39 + "Registro de Venta" + " "*39 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Cabecera de la venta
        gotoxy(5, 5)
        print(f"Factura #: F0999999 {' '*3} Fecha: {datetime.datetime.now()}")

        # Obtener la cédula del cliente
        gotoxy(10, 7)
        dni = validar.solo_numeros("Cédula del cliente: ", 23, 7)

        # Verificar si el cliente existe
        json_file = JsonFile(path+'/archivos/clients.json')
        cliente = json_file.find("cedula", dni)
        if not cliente:
            gotoxy(35, 7)
            print("Cliente no existe.")
            input("Presione una tecla para continuar...")
            return

        # Crear objeto cliente
        cliente = cliente[0]
        cli = RegularClient(cliente["nombre"], cliente["apellido"], cliente["cedula"], card=True)
        sale = Sale(cli)

        # Detalle de la venta
        gotoxy(5, 9)
        print("Linea\tId_Articulo\tDescripción\tPrecio\tCantidad\tSubtotal")
        follow = "s"
        line = 10
        while follow.lower() == "s":
            # Obtener el ID del producto
            gotoxy(7, line)
            print(line - 9)
            gotoxy(15, line)
            id_producto = validar.solo_numeros("ID del artículo: ", 15, line)

            # Buscar el producto por ID
            json_file = JsonFile(path+'/archivos/products.json')
            productos = json_file.find("id", id_producto)
            if not productos:
                gotoxy(24, line)
                print("Producto no encontrado.")
                time.sleep(1)
                gotoxy(24, line)
                print(" "*20)
            else:
                producto = productos[0]
                prod = Product(producto["id"], producto["descripcion"], producto["precio"], producto["stock"])
                gotoxy(24, line)
                print(prod.descripcion)
                gotoxy(38, line)
                print(prod.precio)
                qyt = int(validar.solo_numeros("Cantidad: ", 49, line))
                gotoxy(49, line)
                print(qyt)
                gotoxy(58, line)
                subtotal = prod.precio * qyt
                print(subtotal)
                sale.add_detail(prod, qyt)

                # Actualizar subtotal, descuento, IVA y total
                gotoxy(66, 5)
                print(f"Subtotal: {round(sale.subtotal, 2)}")
                gotoxy(66, 6)
                print(f"Descuento: {round(sale.discount, 2)}")
                gotoxy(66, 7)
                print(f"IVA: {round(sale.iva, 2)}")
                gotoxy(66, 8)
                print(f"Total: {round(sale.total, 2)}")

                # Continuar con la venta
                gotoxy(74, line)
                follow = input("Presione Enter para continuar o 'n' para terminar: ") or "s"
                gotoxy(76, line)
                print(green_color + "✔" + reset_color)
                line += 1

        # Confirmar la venta
        gotoxy(15, line)
        print("¿Está seguro de grabar la venta (s/n): ")
        procesar = input().lower()
        if procesar == "s":
            gotoxy(15, line + 1)
            print("😊 Venta grabada satisfactoriamente 😊")
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            ultima_factura = invoices[-1]["factura"] + 1
            data = sale.getJson()
            data["factura"] = ultima_factura
            invoices.append(data)
            json_file.save(invoices)
        else:
            gotoxy(20, line + 1)
            print("🤣 Venta cancelada 🤣")
        input("Presione una tecla para continuar...")

    # En la clase CrudSales

    def consult(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*38 + "Consultar Ventas" + " "*38 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Leer las ventas desde el archivo JSON
        json_file = JsonFile(path+'/archivos/invoices.json')
        ventas = json_file.read()

        # Mostrar la lista de ventas
        gotoxy(10, 5)
        print("Lista de Ventas:")
        gotoxy(10, 7)
        print("Factura\t\tFecha\t\tCliente\t\tTotal")
        line = 9
        for venta in ventas:
            gotoxy(10, line)
            print(f"{venta['factura']}\t\t{venta['Fecha']}\t\t{venta['cliente']}\t\t{venta['total']}")
            line += 1

        input("Presione una tecla para continuar...")

    def update(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*38 + "Actualizar Venta" + " "*38 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Obtener el número de factura a actualizar
        gotoxy(10, 5)
        factura = input("Ingrese el número de factura a actualizar: ")

        # Buscar la factura por número en el archivo JSON
        json_file = JsonFile(path+'/archivos/invoices.json')
        ventas = json_file.read()
        factura_encontrada = None
        for venta in ventas:
            if str(venta["factura"]) == factura:
                factura_encontrada = venta
                break

        if factura_encontrada:
            # Mostrar los detalles de la factura antes de actualizarla
            gotoxy(10, 7)
            print(f"Factura: {factura_encontrada['factura']}")
            gotoxy(10, 8)
            print(f"Fecha: {factura_encontrada['Fecha']}")
            gotoxy(10, 9)
            print(f"Cliente: {factura_encontrada['cliente']}")
            gotoxy(10, 10)
            print(f"Total: {factura_encontrada['total']}")

            # Obtener los nuevos datos de la factura
            gotoxy(10, 12)
            nuevo_total = float(input("Nuevo total de la factura (deje en blanco para mantener): ") or factura_encontrada["total"])

            # Actualizar el total de la factura
            factura_encontrada["total"] = nuevo_total

            # Guardar los cambios en el archivo JSON
            json_file.save(ventas)
            gotoxy(10, 14)
            print("Factura actualizada exitosamente.")
        else:
            gotoxy(10, 7)
            print("Factura no encontrada.")
        input("Presione una tecla para continuar...")

    def delete(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "█"*90)
        gotoxy(2, 2)
        print("██" + " "*38 + "Eliminar Venta" + " "*38 + "██")
        gotoxy(2, 3)
        print(green_color + "█"*90)

        # Obtener el número de factura a eliminar
        gotoxy(10, 5)
        factura = input("Ingrese el número de factura a eliminar: ")

        # Buscar la factura por número en el archivo JSON
        json_file = JsonFile(path+'/archivos/invoices.json')
        ventas = json_file.read()
        factura_encontrada = None
        for venta in ventas:
            if str(venta["factura"]) == factura:
                factura_encontrada = venta
                break

        if factura_encontrada:
            # Mostrar los detalles de la factura antes de eliminarla
            gotoxy(10, 7)
            print(f"Factura: {factura_encontrada['factura']}")
            gotoxy(10, 8)
            print(f"Fecha: {factura_encontrada['Fecha']}")
            gotoxy(10, 9)
            print(f"Cliente: {factura_encontrada['cliente']}")
            gotoxy(10, 10)
            print(f"Total: {factura_encontrada['total']}")
            gotoxy(10, 12)
            print("¿Está seguro que desea eliminar esta factura?")
            confirmacion = input("Ingrese 's' para confirmar, cualquier otra tecla para cancelar: ")

            if confirmacion.lower() == 's':
                ventas.remove(factura_encontrada)
                json_file.save(ventas)
                gotoxy(10, 14)
                print("Factura eliminada exitosamente.")
            else:
                gotoxy(10, 14)
                print("Eliminación cancelada.")
        else:
            gotoxy(10, 7)
            print("Factura no encontrada.")
        input("Presione una tecla para continuar...")



