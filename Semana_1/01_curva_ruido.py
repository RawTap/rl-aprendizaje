import random
from math import pi, sin

import matplotlib.pyplot as plt
import seaborn as sns


def eje_x(numero):
    lista_x = []
    for i in range(numero):
        randomizar = round(random.uniform(0, 2 * pi), 2)
        lista_x.append(randomizar)
    lista_x.sort()
    return lista_x


def eje_y(lista_x):
    lista_y = []
    for i in lista_x:
        lista_y.append(sin(i))
    return lista_y


def crear_ruido(numero, porcentaje=0.15):
    lista_ruido = []
    for i in numero:
        ruido = random.uniform(-porcentaje * i, porcentaje * i)
        lista_ruido.append(ruido)
    return lista_ruido


def agregar_ruido(eje_y, ruido):
    y_ruidosa = []
    for i in range(len(eje_y)):
        y_ruidosa.append(eje_y[i] - ruido[i])
    return y_ruidosa


numero = 50
x = eje_x(numero)
y = eje_y(x)

r = agregar_ruido(y, crear_ruido(y))

# tema seaborn
sns.set_theme(style="darkgrid")

# seno limpio
sns.lineplot(x=x, y=y, color="blue", label="Seno limpio")

# seno ruidoso
sns.scatterplot(x=x, y=r, color="red", label="seno ruidoso")

plt.title("Seno vs Seno ruidoso", fontsize=14)
plt.xlabel("Eje X (Radianes)")
plt.ylabel("Eje Y (Seno)")
plt.legend()

plt.show()
