inventario = []

def nuevo_prod():
    nombre = input("Digite el nombre del producto: ")
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"\nEl producto '{nombre}' ya existe en el inventario.")
            print("¿Desea actualizar el producto existente?")
            opcion = input("Digite 'S' para actualizar o cualquier otra tecla para cancelar: ").lower()
            
            if opcion == "s":
                update_prod()
            else:
                print("Operación cancelada. No se agregó el producto.")
            return 
    
    precio = float(input("Digite el precio del producto: "))
    cantidad = int(input("Digite la cantidad del producto: "))
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("Producto agregado con éxito.")

def show_inv():
    if inventario:
        print("\nInventario actual:")
        for i, producto in enumerate(inventario, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("\nEl inventario está vacío.")
        
def rest_prod():
    prod = input("Digite el nombre del producto que desea eliminar: ")
    
    for producto in inventario:
        if producto["nombre"].lower() == prod.lower():
            inventario.remove(producto)
            print(f"El producto '{prod}' ha sido eliminado.")
            return
    
    print(f"El producto '{prod}' no se encontró en el inventario.")

def update_prod():
    prod = input("Digite el nombre del producto que desea actualizar: ")
    
    for producto in inventario:
        if producto["nombre"].lower() == prod.lower():
            print(f"\nProducto encontrado: {producto}")
            
            
            print("¿Qué desea actualizar?")
            print("1. Precio")
            print("2. Cantidad")
            print("3. Ambos")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nuevo_precio = float(input("Digite el nuevo precio: "))
                producto["precio"] = nuevo_precio
                print(f"Precio actualizado a {nuevo_precio}.")
                
            elif opcion == "2":
                nueva_cantidad = int(input("Digite la nueva cantidad: "))
                producto["cantidad"] = nueva_cantidad
                print(f"Cantidad actualizada a {nueva_cantidad}.")
                
            elif opcion == "3":
                nuevo_precio = float(input("Digite el nuevo precio: "))
                nueva_cantidad = int(input("Digite la nueva cantidad: "))
                producto["precio"] = nuevo_precio
                producto["cantidad"] = nueva_cantidad
                print(f"Producto actualizado: Precio = {nuevo_precio}, Cantidad = {nueva_cantidad}.")
                
            else:
                print("Opción no válida. Intente nuevamente.")
            
            return  
        
    print(f"El producto '{prod}' no se encontró en el inventario.")


while True:
    print("\nOpciones:")
    print("1. Agregar un nuevo producto")
    print("2. Mostrar el inventario")
    print("3. Restar productos")
    print("4. Actualizar un producto")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nuevo_prod()
    elif opcion == "2":
        show_inv()
    elif opcion == "3":
        rest_prod()
    elif opcion == "4":
        update_prod()
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")