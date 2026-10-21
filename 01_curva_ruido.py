import random
from math import pi, sin

import matplotlib.pyplot as plt
import seaborn as sns


def eje_x(numero):
    lista_x = []
    for i in range(numero):
        randomizar = round(random.uniform(0, 2 * pi), 2)
        lista_x.append(randomizar)
    return lista_x


def eje_y(lista_x):
    lista_y = []
    for i in lista_x:
        lista_y.append(sin(i))
    return lista_y


x = eje_x(50)
y = eje_y(x)

# Usar seaborn
sns.set_theme(style="darkgrid")

sns.scatterplot(x=x, y=y, color="crimson", s=70)

plt.title("Gráfica de y = sin(x) con Seaborn", fontsize=14)
plt.xlabel("Eje X (Radianes)")
plt.ylabel("Eje Y (Seno)")

plt.show()
# plt.scatter(x, y, color="green")
# plt.title("Grafica de y = sin(x) en puntos aleatorios")
# plt.xlabel("Eje x en radianes")
# plt.ylabel("Eje Y")
# plt.grid(True)

# plt.show()
