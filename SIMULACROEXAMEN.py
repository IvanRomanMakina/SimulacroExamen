MENU = """
Seleccione el numero de alguna de las siguientes opciones:
1) Cargar producto/s
2) Buscar producto
3) Ordenar inventario
4) Mostrar producto más caro
5) Mostrar producto más barato
6) Mostrar productos con precio mayor a 15000
7) Salir
"""

inventario = [
        ["Laptop",1500.00,10],
        ["Silla",200.00,50],
        ["Libro",15.00,100],
        ["Monitor",300.00,30]
]

def mostrar_menu(MENU:str) -> int:
    """Muestra el menú principal y devuelve la opción seleccionada."""
    print(MENU)

def cargar_inventario():
    """Permite al usuario cargar productos en el inventario."""
    cantidad = int(input("¿Cuántos productos desea ingresar? "))
    for _ in range(cantidad):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        inventario.append([nombre, precio, cantidad_producto])

def buscar_producto():
    """Busca un producto por su nombre y muestra sus detalles."""
    nombre = input("Ingrese el nombre del producto a buscar: ")
    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            print(f"Producto encontrado: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")
            return
    print("Producto no encontrado.")

def ordenar_inventario():
    """Ordena el inventario por precio de manera ascendente."""
    if not inventario:
        print("No hay productos registrados.")
        return
    n = len(inventario)
    for i in range(n):
        for j in range(0, n-i-1):
            if inventario[j][1] > inventario[j+1][1]:
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j] 

    print("Inventario ordenado por precio:")
    for producto in inventario:
        print(f"Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")

def mostrar_producto_mas_caro():
    """Muestra el producto más caro en el inventario."""
    producto_caro = None

    for producto in inventario:
        if producto_caro is None or producto[1] > producto_caro[1]: 
            producto_caro = producto

    if producto_caro:
        print(f"Producto más caro: {producto_caro[0]}, Precio: {producto_caro[1]}, Cantidad: {producto_caro[2]}")
    else:
        print("No hay productos registrados.")

def mostrar_producto_mas_barato():
    """Muestra el producto más barato en el inventario."""
    producto_barato = None 

    for producto in inventario:
        if producto_barato is None or producto[1] < producto_barato[1]:
            producto_barato = producto

    if producto_barato:
        print(f"Producto más barato: {producto_barato[0]}, Precio: {producto_barato[1]}, Cantidad: {producto_barato[2]}")
    else:
        print("No hay productos registrados.")


def mostrar_productos_precio_mayor_a_15000():
    """Muestra los productos con un precio mayor a 15000."""
    productos_encontrados = [producto for producto in inventario if producto[1] > 15000]
    if productos_encontrados:
        print("Productos con precio mayor a 15000:")
        for producto in productos_encontrados:
            print(f"Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")
    else:
        print("No hay productos con precio mayor a 15000.")

def ejecutar_opcion(seguir:bool) -> bool:
    """
    Recibe parametro "seguir" (bool), se le pregunta un numero de opcion y ejecuta esa opcion(funcion) o finaliza el programa.
    Parametros: seguir (bool)
    Salida: seguir (bool)
    """
    opcion = int(input("Elige una opcion: "))
    while opcion < 1 or opcion > 7: 
        print("Opcion no valida")
        opcion = int(input("Elige una opcion(1-7): "))
    if opcion == 1:
        print("Haz elegido la opcion 1")
        cargar_inventario()
        seguir = True
    elif opcion == 2:
        print("Haz elegido la opcion 2")
        buscar_producto()
        seguir = True
    elif opcion == 3:
        print("Haz elegido la opcion 3")
        ordenar_inventario()
        seguir = True
    elif opcion == 4:
        print("Haz elegido la opcion 4")
        mostrar_producto_mas_caro()
        seguir = True
    elif opcion == 5:
        print("Haz elegido la opcion 5")
        mostrar_producto_mas_barato()
        seguir = True
    elif opcion == 6:
        print("Haz elegido la opcion 6")
        mostrar_productos_precio_mayor_a_15000()
        seguir = True        
    else:
        print("Haz elegido la opcion 7. Haz salido del sistema.")
        seguir = False
    return seguir

seguir = True
while seguir == True:
    mostrar_menu(MENU)
    seguir = ejecutar_opcion(seguir)