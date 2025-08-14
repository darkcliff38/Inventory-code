import tkinter as tk
from tkinter import messagebox
import json



# Funciones para manejar el inventario
def agregar_producto(nombre, cantidad, precio): # Agrega un nuevo producto al inventario
    nombre_estandrizado = nombre.strip().lower() # Estandariza el nombre del producto
    nuevo_producto = {"nombre": nombre_estandrizado, "cantidad": cantidad, "precio": precio}
    inventario.append(nuevo_producto)
    actualizar_listbox()

def eliminar_producto(nombre): # Elimina un producto del inventario por nombre
    global inventario
    nombre_estandrizado = nombre.strip().lower()  # Estandariza el nombre del producto
    inventario = [producto for producto in inventario if producto["nombre"] != nombre_estandrizado]


def actualizar_producto(nombre, cantidad, precio): # Actualiza un producto existente en el inventario
    for producto in inventario:
        if producto["nombre"] == nombre:
            producto["cantidad"] = cantidad
            producto["precio"] = precio
            return
    

def buscar_producto(nombre): # Busca un producto en el inventario por nombre
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None

def manejar_click_boton_agregar(): # Maneja el evento de clic en el botón para agregar un producto
    try:
        nombre_producto = entry_nombre.get().strip()
        cantidad_producto = int(entry_cantidad.get())
        precio_producto = float(entry_precio.get())
        if not nombre_producto:
            messagebox.showerror("Error", "Por favor, ingresa un nombre de producto.")
            return
        if cantidad_producto <= 0 or precio_producto <= 0:
            messagebox.showerror("Error", "La cantidad y el precio deben ser mayores a cero.")
            return
        agregar_producto(nombre_producto, cantidad_producto, precio_producto)
        messagebox.showinfo("Exito", f"Producto agregado: {nombre_producto}, Cantidad: {cantidad_producto}, Precio: {precio_producto}")
    except ValueError:
        messagebox.showerror("Error", "Asegúrate de ingresar una cantidad con numero entero y un precio válido.")
    

def borrar_placeholder(event, entry, placeholder_text=""): # Borra el texto de marcador de posición cuando el usuario hace clic en el campo de entrada
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.config(fg='black')
    
def mostrar_inventario_gui(): # Muestra el inventario actual en la consola
    print("---Inventario actual:---")
    for producto in inventario:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
    print("-------------------------")

def actualizar_listbox(): # Actualiza el Listbox con los productos del inventario
    listbox_inventario.delete(0, tk.END)  # Borra todos los elementos de la lista
    for producto in inventario: # Recorre el inventario y agrega cada producto al Listbox
        listbox_inventario.insert(tk.END, f"Nombre: {producto['nombre'].title()}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
        
def obtener_producto_seleccionado(event): # Obtiene el producto seleccionado en el Listbox
    try:
        indice = listbox_inventario.curselection()[0]
        producto_seleccionado = inventario[indice]
        return producto_seleccionado
    except IndexError:
        messagebox.showerror("Error", "No se ha seleccionado ningún producto.")
        return None
    
def manejar_click_boton_eliminar(): # Maneja el evento de clic en el botón para eliminar un producto
    producto =  obtener_producto_seleccionado(event=None)
    if producto:
        eliminar_producto(producto["nombre"])
        messagebox.showinfo("Exito", f"Producto eliminado: {producto['nombre']}")
        actualizar_listbox()
    else:
        messagebox.showerror("Error", "No se pudo eliminar el producto, no se seleccionó ninguno.")

def manejar_click_boton_actualizar(): # Maneja el evento de clic en el botón para actualizar un producto
    producto = obtener_producto_seleccionado(event=None)
    if producto:
        try:
            nombre = producto["nombre"]
            nueva_cantidad = int(entry_cantidad.get())
            nuevo_precio = float(entry_precio.get())
            actualizar_producto(nombre, nueva_cantidad, nuevo_precio)
            messagebox.showinfo("Exito", f"Producto actualizado: {nombre}, Nueva Cantidad: {nueva_cantidad}, Nuevo Precio: {nuevo_precio}")
            actualizar_listbox()
        except ValueError:
            messagebox.showerror("Error", "Asegúrate de ingresar una cantidad con numero entero y un precio válido.")
    else:
        messagebox.showerror("Error", "No se pudo actualizar el producto, no se seleccionó ninguno.")

def rellenar_campos(producto): # Rellena los campos de entrada con los datos del producto seleccionado
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

    entry_nombre.insert(0, producto["nombre"])
    entry_cantidad.insert(0, str(producto["cantidad"]))
    entry_precio.insert(0, str(producto["precio"]))

def seleccionar_producto(event): # Evento para seleccionar un producto del Listbox
    producto = obtener_producto_seleccionado(event)
    if producto:
        rellenar_campos(producto)

def manejar_click_boton_buscar(): # Maneja el evento de clic en el botón para buscar un producto
    nombre_a_buscar = entry_nombre.get().strip().lower()
    if nombre_a_buscar:
        producto_encontrado = buscar_producto(nombre_a_buscar)
        if producto_encontrado:
            messagebox.showinfo("Producto Encontrado", f"Nombre: {producto_encontrado['nombre'].title()}, Cantidad: {producto_encontrado['cantidad']}, Precio: {producto_encontrado['precio']}")
        else:
            messagebox.showerror("Producto No Encontrado", f"No se encontró el producto con nombre: {nombre_a_buscar}")
    else:
        messagebox.showerror("Error", "Por favor, ingresa un nombre de producto para buscar.")

def limpiar_campos(): # Limpia los campos de entrada
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    
    entry_nombre.insert(0, "Nombre del producto")
    entry_cantidad.insert(0, "Cantidad del producto")
    entry_precio.insert(0, "Precio del producto")

    entry_nombre.config(fg='grey')
    entry_cantidad.config(fg='grey')
    entry_precio.config(fg='grey')

def guardar_inventario(): # Guarda el inventario en un archivo JSON
    try:
        with open("inventario.json", "w") as archivo:
            json.dump(inventario, archivo, indent=4)
            messagebox.showinfo("Exito", "Inventario guardado correctamente en inventario.json")
    except IOError:
        messagebox.showerror("Error", "No se pudo guardar el inventario.")
    finally:
        ventana.destroy()  # Cierra la ventana al guardar el inventario

def cargar_inventario(): # Carga el inventario desde un archivo JSON
    global inventario

    inventario_inicial = [
    {"nombre": "manzanas", "cantidad": 10, "precio": 500.0},
    {"nombre": "peras", "cantidad": 5, "precio": 350.0},
    {"nombre": "naranjas", "cantidad": 8, "precio": 400.0},
    {"nombre": "platanos", "cantidad": 12, "precio": 200.0},
    {"nombre": "uvas", "cantidad": 15, "precio": 600.0}
]
    try: 
        with open("inventario.json", "r") as archivo:
            inventario = json.load(archivo)
            messagebox.showinfo("Exito", "Inventario cargado correctamente desde inventario.json")
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo inventario.json no existe. No se pudo cargar el inventario. Se utilizará el inventario predeterminado.")
        inventario = inventario_inicial  # Si no existe el archivo, usa el inventario inicial
    except json.JSONDecodeError:
        messagebox.showerror("Error", "El archivo inventario.json está corrupto o no es un JSON válido. No se pudo cargar el inventario. Se utilizará el inventario predeterminado.")
        inventario = inventario_inicial  # Si hay un error al leer el archivo, usa el inventario inicial
        
        
        
cargar_inventario()  # Carga el inventario al iniciar la aplicación

# Interfaz gráfica para el sistema de inventario
ventana = tk.Tk()
ventana.title("Sistema de Inventario")
ventana.geometry("800x600")

frame_izquierda = tk.Frame(ventana, padx=10, pady=10) # frame izquierda para los botones y campos de entrada
frame_izquierda.pack(side=tk.LEFT, fill=tk.BOTH)

frame_derecha = tk.Frame(ventana, padx=10, pady=10) # frame derecha para el Listbox y la barra de desplazamiento
frame_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

frame_campos = tk.Frame(frame_izquierda) 
frame_campos.pack(fill=tk.X, pady=10)


entry_nombre = tk.Entry(frame_campos) 
entry_nombre.pack(fill=tk.X, expand=True)
entry_nombre.insert(0, "Nombre del producto")
entry_nombre.config(fg='grey')
entry_nombre.bind("<FocusIn>", lambda event: borrar_placeholder(event, entry_nombre, "Nombre del producto"))

entry_cantidad = tk.Entry(frame_campos)
entry_cantidad.pack(fill=tk.X, expand=True)
entry_cantidad.insert(0, "Cantidad del producto")
entry_cantidad.config(fg='grey')
entry_cantidad.bind("<FocusIn>", lambda event: borrar_placeholder(event, entry_cantidad, "Cantidad del producto"))

entry_precio = tk.Entry(frame_campos)
entry_precio.pack(fill=tk.X, expand=True)
entry_precio.insert(0, "Precio del producto")
entry_precio.config(fg='grey')
entry_precio.bind("<FocusIn>", lambda event: borrar_placeholder(event, entry_precio, "Precio del producto"))


tk.Button(frame_campos, text="limpiar", command=limpiar_campos).pack(padx=5)

tk.Button(frame_izquierda, text="Agregar Producto", command=manejar_click_boton_agregar).pack()

tk.Button(frame_izquierda, text="Mostrar Inventario (Consola)", command=mostrar_inventario_gui).pack()

tk.Button(frame_izquierda, text="Eliminar Producto Seleccionado", command=manejar_click_boton_eliminar).pack()

tk.Button(frame_izquierda, text="Actualizar Producto Seleccionado", command=manejar_click_boton_actualizar).pack()

tk.Button(frame_izquierda, text="Buscar Producto", command=manejar_click_boton_buscar).pack()


listbox_inventario = tk.Listbox(frame_derecha, height=15, width=50)
listbox_inventario.pack(side=tk.RIGHT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame_derecha, orient=tk.VERTICAL, command=listbox_inventario.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_inventario.config(yscrollcommand=scrollbar.set)

listbox_inventario.bind('<<ListboxSelect>>', seleccionar_producto) # Vincula el evento de selección del Listbox a la función seleccionar_producto

ventana.protocol("WM_DELETE_WINDOW", guardar_inventario) # Guarda el inventario al cerrar la ventana

actualizar_listbox()
ventana.mainloop()
