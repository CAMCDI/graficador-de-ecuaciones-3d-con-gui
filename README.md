# Graficador de Ecuaciones en 3D

Este es un proyecto de Python que permite a los usuarios graficar ecuaciones en 3D a partir de su entrada. Utiliza la biblioteca `matplotlib` para crear gráficos en 3D y la biblioteca `tkinter` para la interfaz gráfica. Los usuarios pueden ingresar una ecuación de la forma `Z = f(X, Y)` y visualizar su gráfico en 3D.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes bibliotecas:

- `numpy`
- `matplotlib`
- `tkinter` (generalmente viene preinstalada con Python, pero asegúrate de tenerla disponible)

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install numpy matplotlib
```

## Descripción del Script

1. **Interfaz Gráfica (Tkinter)**: La aplicación utiliza `tkinter` para crear una ventana donde el usuario puede ingresar una ecuación que dependa de las variables `X` e `Y`. La interfaz consta de:
   - Un campo de texto donde el usuario puede ingresar la ecuación.
   - Un botón para graficar la ecuación.
   
2. **Graficado de la Ecuación (Matplotlib)**: Después de ingresar la ecuación, la función `graficar_ecuacion` se encarga de:
   - Crear una malla de puntos para los valores de `X` e `Y` dentro del rango [-5, 5].
   - Evaluar la ecuación en cada punto de la malla utilizando `eval`.
   - Generar un gráfico 3D utilizando `matplotlib` y mostrarlo en una ventana emergente.

3. **Manejo de Errores**: Si ocurre un error al graficar la ecuación (por ejemplo, si la ecuación no es válida o si hay un problema con los valores de entrada), se muestra un mensaje de error utilizando un cuadro de mensaje de `tkinter`.

## Cómo Usar

1. **Ejecuta el Script**: Simplemente corre el script en tu entorno de desarrollo Python.
2. **Introduce la Ecuación**: En la ventana de la aplicación, introduce una ecuación en términos de `X` e `Y`. Por ejemplo, puedes ingresar una ecuación como:
   ```python
   X**2 + Y**2
   ```
   o cualquier ecuación matemática válida en función de `X` e `Y`.
3. **Graficar la Ecuación**: Haz clic en el botón "Graficar" para generar y mostrar el gráfico 3D de la ecuación ingresada.

## Ejemplo de Uso

1. Ingresar `X**2 + Y**2` en el campo de entrada.
2. Al hacer clic en "Graficar", aparecerá una representación 3D de un paraboloide.

## Problemas Comunes

- **Error al graficar**: Si el programa muestra un mensaje de error, verifica que la ecuación esté correctamente escrita en términos de `X` e `Y`. Asegúrate de que no haya errores tipográficos.
- **Ecuaciones complejas**: Si deseas graficar ecuaciones más complejas, como funciones trigonométricas o logaritmos, asegúrate de utilizar las funciones matemáticas estándar en Python, por ejemplo, `np.sin(X)`, `np.log(X)`, etc.

## Contribuciones

Si deseas mejorar este proyecto o agregar nuevas características, siéntete libre de hacer un pull request. Algunas ideas de mejora podrían incluir:
- La capacidad de personalizar el rango de los valores de `X` e `Y`.
- Soporte para otras funciones matemáticas o incluso ecuaciones paramétricas.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
