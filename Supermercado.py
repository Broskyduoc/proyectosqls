import os

if os.path.basename(os.getcwd()) != 'Supermercado':
    os.chdir('Supermercado')

def valNum(n):
    try:
        int(n)
        return True
    except Exception:
        return False
def clp(n):
    return f"${int(n):,}".replace(",", ".")

# salas = '🏃➡⚽🥅👑👑👑'
# DEFINIR VARIABLES -----------------------------------------------------------------------------------------------------
anchoPagina = 100
# LOL




def espacios(texto,anchoPagina):
    return int((anchoPagina - len(texto))/2)

def clear():
    if os.name == "nt": #windows
        os.system('cls')
    else: #linux
        os.system('clear')

def actualizarContabilidad():
    with open('contabilidad.txt', 'r') as file:
        return file.readlines()
    
def actualizarVentas():
    with open('ventas.txt', 'r') as file:
        return file.readlines()

def menuPrincipal():
    # Inventario = Registra productos, actualización de productos, entrada de stock -
    # - salida de stock, consultar inventario, buscar producto por nombre y categoría -
    # - (ej: bebidas, lácteos, limpieza), eliminar inventario, calcular valor total del inventario.
    clear()
    r = input(
        'Menu principal\n\n' \
        '1. Consultar stock\n' \
        '2. Agregar stock\n' \
        '3. Modificar stock\n' \
        '4. Ventas\n' \
        '5. Contabilidad\n' \
        '6. Salir\n'
    )
    
    if r == "1":
        consultarStock(getInv(), anchoPagina)
    elif r == "2":
        agregarStock()
    elif r == "3":
        modificarStock()
    elif r == "4":
        mostrarVentas()
    elif r == "5":
        menuContabilidad()
    elif r == "6":
        clear()
        print("Cerrando programa...")
    else:
        menuPrincipal()


def agregarStock():   # DEJAR AL USUARIO AGREGAR STOCK
    os.system('cls')
    r = input(
        'Agregar stock\n\n' \
        '1. Agregar producto nuevo\n' \
        '2. Reponer producto existente\n' \
        '3. Volver al menu principal\n'
    )
    if r == "1":
        agregarProducto()
    elif r == "2":
        reponerProducto()
    elif r == "3":
        menuPrincipal()
    else:
        agregarStock()

def agregarProducto():
    inventario = getInv()
    
    


# --------------------------------------------------------------------------------------------------------------
# FUNCIONES DE UTILIDAD
def getInv():
    inventario = []
    with open('inventario.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            partes = [p.strip() for p in line.split(',')]
            if partes[0].lower() == 'inventario':  # ignorar encabezado
                continue
            if len(partes) < 6:
                continue
            id = partes[0]
            nombre = partes[1]
            compra = partes[2]
            venta = partes[3]
            stock = partes[4]
            categorias = partes[5:]
            producto = [id, nombre, compra, venta, stock, categorias]
            inventario.append(producto)
    return inventario

def saveInv(inventario):   # GUARDAR INFORMACION DEL INVENTARIO
    with open('inventario.txt', 'w') as file:
        for item in inventario:
            linea = ','.join(str(elemento) for elemento in item)
            file.write(linea)



def consultarStock(inventario,anchoPagina):   # MOSTRAR STOCK AL USUARIO
    clear()
    tmpPag = espacios('STOCK ACTUAL', anchoPagina)
    print(f"{'-'*tmpPag}STOCK ACTUAL{'-'*tmpPag}")
    print(f"{' '*espacios('Pag 1', anchoPagina)}Pag 1\n")

    espacioRes = anchoPagina
    inventario = getInv()


    for producto in inventario:
        id = producto[0]
        nombre = producto[1]
        compra = producto[2]
        venta = producto[3]
        cantidad = producto[4]
        categorias = ", ".join(producto[5])
        tmp = 3 - len(str(id))
        tmpLinea = [(f"{id}{' '*tmp}|")]
        tmp = 35 - len(nombre)
        tmpLinea.append((f"{" "*tmp}{nombre}|"))
        tmp = 9 - len(clp(compra))
        tmpLinea.append((f"{" "*tmp}{clp(compra)}|"))
        tmp = 9 - len(clp(venta))
        tmpLinea.append((f"{" "*tmp}{clp(venta)}|"))
        tmp = 9 - len(cantidad)
        tmpLinea.append((f"{" "*tmp}{cantidad}|"))
        tmp = 30 - len(categorias)
        tmpLinea.append((f"{" "*tmp}{categorias}"))
        

        linea = "".join(tmpLinea)
        print(linea)
        print(f"---+{"-"*35}+{"---------+"*3}+{"-"*29}")




def modificarStock(inventario):
    producto = input("Nombre del producto a eliminar: ").lower()

    if producto in inventario:
        confirmar = input(f"¿Estás seguro de eliminar el producto: {producto} del inventario?").lower()

        if confirmar == "s":
            del inventario[producto]
            print(f"Producto {producto} eliminado del inventario.")
        else:
            print("Operación cancelada")
    else:
        print("Error - Producto no existe en el stock actual")

def mostrarVentas(inventario):
    pass

menuPrincipal()


