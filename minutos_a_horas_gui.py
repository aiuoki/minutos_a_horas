import tkinter as tk

def convertir():
    try:
        minutos = int(entry_minutos.get())
        horas = minutos // 60
        minutos_resto = minutos % 60
        resultado_text = f"{minutos} Minutos = {horas} Horas"
        if minutos_resto != 0:
            resultado_text = f"{minutos} Minutos = {round(minutos / 60, 2)} Horas = {horas} Horas y {minutos_resto} Minutos"
        resultado.config(text=resultado_text)  # Actualizar el texto del Label con el resultado
    except ValueError:
        resultado.config(text="Por favor, introduce un número válido de minutos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Minutos a Horas")
root.geometry("400x160")
root.eval('tk::PlaceWindow . center')

# Etiqueta y entrada para los minutos
label_minutos = tk.Label(root, text="Minutos:")
label_minutos.pack(pady=5)
entry_minutos = tk.Entry(root, width=10)
entry_minutos.pack()

# Botón para convertir
button_convertir = tk.Button(root, text="Convertir", command=convertir)
button_convertir.pack(pady=10)

# Resultado debajo del input
resultado = tk.Label(root, text="", wraplength=350)
resultado.pack(pady=10)

# Ejecutar el bucle principal de la ventana
root.mainloop()