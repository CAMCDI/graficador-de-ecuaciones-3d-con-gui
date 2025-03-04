import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def graficar_ecuacion():
    # Obtener la ecuación de la entrada del usuario
    ecuacion = entry_ecuacion.get()

    try:
        # Definir el rango de valores para x e y
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)

        # Crear una malla de puntos (x, y)
        X, Y = np.meshgrid(x, y)

        # Evaluar la ecuación en los puntos X y Y
        # Usamos eval para calcular z con la ecuación ingresada
        Z = eval(ecuacion)

        # Crear la figura y los ejes 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Graficar la superficie
        ax.plot_surface(X, Y, Z, cmap='viridis')

        # Etiquetas de los ejes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Mostrar el gráfico
        plt.show()

    except Exception as e:
        # Si ocurre algún error, mostrar un mensaje
        messagebox.showerror("Error", f"Hubo un error al graficar la ecuación: {e}")

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Graficador de Ecuaciones en 3D")

# Crear una etiqueta y un campo de entrada para la ecuación
label_ecuacion = tk.Label(root, text="Introduce la ecuación de Z (en términos de X e Y):")
label_ecuacion.pack(padx=10, pady=5)

entry_ecuacion = tk.Entry(root, width=50)
entry_ecuacion.pack(padx=10, pady=5)

# Botón para graficar
btn_graficar = tk.Button(root, text="Graficar", command=graficar_ecuacion)
btn_graficar.pack(padx=10, pady=20)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
