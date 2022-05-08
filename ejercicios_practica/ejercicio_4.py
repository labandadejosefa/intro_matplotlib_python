# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
#from cProfile import label #----------Comenté esta línea, porque arrojaba error!
#from turtle import color #-----------Comenté esta línea, porque arrojaba error!
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

    figu = plt.figure()
    st = figu.suptitle('Comparación del crecimiento de funciones', fontsize=13)

    ax1 = figu.add_subplot(2,2,1)
    ax1.plot(x, y1, color = 'teal',label= r'$f_{1}(x)$ = $x^{2}$')
    ax1.set_facecolor('whitesmoke')
    ax1.grid(ls ='--')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.legend()
    
    ax2 = figu.add_subplot(2,2,2)
    ax2.plot(x, y2, color = 'purple',label= r'$f_{2}(x)$ = $x^{3}$')
    ax2.set_facecolor('whitesmoke')
    ax2.grid(ls ='-.')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.legend()

    ax3 = figu.add_subplot(2,2,3)
    ax3.plot(x, y3, color = 'darkorange',label= r'$f_{3}(x)$ = $x^{4}$')
    ax3.set_facecolor('floralwhite')
    ax3.grid('solid')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.legend()


    ax4 = figu.add_subplot(2,2,4)
    ax4.plot(x, y4, color = 'k',label= r'$f_{4}(x)$ = $\sqrt{x}$')
    ax4.set_facecolor('floralwhite')
    ax4.grid(ls =':')
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.legend()

    
    plt.show() 


    print("terminamos")
