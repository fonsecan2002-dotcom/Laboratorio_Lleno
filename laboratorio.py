import tkinter as tk
from tkinter import messagebox

# -----------------------------------
# VARIABLES
# -----------------------------------
capacidad_maxima = 5
cantidad_estudiantes = 0

# Lista de estudiantes
lista_estudiantes = []

# -----------------------------------
# FUNCION INGRESAR
# -----------------------------------
def ingresar():

    global cantidad_estudiantes

    nombre = txt_nombre.get()

    # Validar nombre
    if nombre == "":
        messagebox.showwarning(
            "Error",
            "Ingrese el nombre del estudiante"
        )
        return

    # Verificar capacidad
    if cantidad_estudiantes < capacidad_maxima:

        cantidad_estudiantes += 1

        # Agregar a lista
        lista_estudiantes.append(nombre)

        # Mostrar en Listbox
        listbox_estudiantes.insert(
            tk.END,
            nombre
        )

        # Actualizar contador
        lbl_cantidad.config(
            text=str(cantidad_estudiantes)
        )

        messagebox.showinfo(
            "Ingreso",
            f"Bienvenido {nombre}"
        )

        txt_nombre.delete(0, tk.END)

        # Verificar capacidad máxima
        if cantidad_estudiantes == capacidad_maxima:

            lbl_estado.config(
                text="LABORATORIO LLENO",
                bg="red",
                fg="white"
            )

            btn_ingresar.config(
                state=tk.DISABLED
            )

# -----------------------------------
# FUNCION SALIR
# -----------------------------------
def salir():

    global cantidad_estudiantes

    # Verificar selección
    seleccion = listbox_estudiantes.curselection()

    if not seleccion:
        messagebox.showwarning(
            "Error",
            "Seleccione un estudiante"
        )
        return

    # Obtener posición seleccionada
    indice = seleccion[0]

    # Obtener nombre
    estudiante = listbox_estudiantes.get(indice)

    # Eliminar del Listbox
    listbox_estudiantes.delete(indice)

    # Eliminar de la lista
    lista_estudiantes.remove(estudiante)

    # Reducir contador
    cantidad_estudiantes -= 1

    lbl_cantidad.config(
        text=str(cantidad_estudiantes)
    )

    messagebox.showinfo(
        "Salida",
        f"{estudiante} salió del laboratorio"
    )

    # Liberar espacio
    if cantidad_estudiantes < capacidad_maxima:

        lbl_estado.config(
            text="DISPONIBLE",
            bg="green",
            fg="white"
        )

        btn_ingresar.config(
            state=tk.NORMAL
        )

# -----------------------------------
# VENTANA PRINCIPAL
# -----------------------------------
ventana = tk.Tk()

ventana.title("CONTROL LABORATORIO")

ventana.geometry("500x500")

ventana.config(bg="white")

# -----------------------------------
# TITULO
# -----------------------------------
titulo = tk.Label(
    ventana,
    text="CONTROL DE LABORATORIO",
    font=("Arial", 18, "bold"),
    bg="white"
)

titulo.pack(pady=10)

# -----------------------------------
# NOMBRE
# -----------------------------------
lbl_nombre = tk.Label(
    ventana,
    text="Nombre del estudiante",
    font=("Arial", 12),
    bg="white"
)

lbl_nombre.pack()

txt_nombre = tk.Entry(
    ventana,
    width=30,
    font=("Arial", 12)
)

txt_nombre.pack(pady=10)

# -----------------------------------
# BOTON INGRESAR
# -----------------------------------
btn_ingresar = tk.Button(
    ventana,
    text="INGRESAR",
    font=("Arial", 12, "bold"),
    bg="lightgreen",
    width=15,
    command=ingresar
)

btn_ingresar.pack(pady=10)

# -----------------------------------
# CONTADOR
# -----------------------------------
lbl_texto = tk.Label(
    ventana,
    text="Cantidad de estudiantes",
    font=("Arial", 14),
    bg="white"
)

lbl_texto.pack()

lbl_cantidad = tk.Label(
    ventana,
    text="0",
    font=("Arial", 30, "bold"),
    fg="blue",
    bg="white"
)

lbl_cantidad.pack()

# -----------------------------------
# LISTA ESTUDIANTES
# -----------------------------------
lbl_lista = tk.Label(
    ventana,
    text="Estudiantes en el laboratorio",
    font=("Arial", 12, "bold"),
    bg="white"
)

lbl_lista.pack(pady=10)

listbox_estudiantes = tk.Listbox(
    ventana,
    width=40,
    height=8,
    font=("Arial", 11)
)

listbox_estudiantes.pack()

# -----------------------------------
# BOTON SALIR
# -----------------------------------
btn_salir = tk.Button(
    ventana,
    text="SALIR ESTUDIANTE",
    font=("Arial", 12, "bold"),
    bg="tomato",
    width=20,
    command=salir
)

btn_salir.pack(pady=15)

# -----------------------------------
# ESTADO
# -----------------------------------
lbl_estado = tk.Label(
    ventana,
    text="DISPONIBLE",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    width=25
)

lbl_estado.pack(pady=20)

# -----------------------------------
# EJECUTAR
# -----------------------------------
ventana.mainloop()