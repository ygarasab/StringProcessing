from time import  perf_counter_ns
import pandas as pd
import seaborn as sns
from os import listdir
from sys import argv
import matplotlib.pyplot as plt
from algoritmos import *

def timeit(fun, args):
    """
    Retorna o tempo de execução de uma função
    :param function fun:
    :param list args:
    :return float:
    """
    start = perf_counter_ns()
    fun(*args)
    end = perf_counter_ns()

    return end - start


funcs = {

    "Força Bruta": forca_bruta,
    "BMH": bmh,
    "BMHS": bmhs,
    "Shift-And Exato": shift_and,
    "Shift-And Aproximado": shift_and_aprox

}

data = []

tamanhos = [500, 1000, 1500, 2000, 5000]

k = 500

if len(argv )> 1: k = int(argv[1])

for tamanho in tamanhos:

    print(f"Iniciando busca em textos de tamanho {tamanho}")

    text = open(f"samples/{tamanho}.lorem", "r").read()

    for algoritmo in funcs.keys():

        print(f"    Buscando com o uso de {algoritmo}")

        linha = {
            "Tamanho" : tamanho,
            "Algoritmo" : algoritmo,
            "Tempo" : 0
        }

        for _ in range(k):

            linha["Tempo"] += timeit(funcs[algoritmo], ['doll', text]) / k

        data.append(linha)

print("Tudo pronto, carregando resultados")

frame = pd.DataFrame(data)

n = len(listdir('datasets')) + 1

frame.to_csv(f"datasets/dataset{ n }.csv")

plot1 = sns.barplot(x = frame["Tamanho"], y = frame["Tempo"], hue=frame["Algoritmo"]).get_figure()
plot1.savefig(f"figuras/figura{ n }-1.png")

frame2 = frame[frame["Algoritmo"] != "Shift-And Aproximado"]

plt.clf()

plot2 = sns.barplot(x = frame2["Tamanho"], y = frame2["Tempo"], hue=frame2["Algoritmo"]).get_figure()
plot2.savefig(f"figuras/figura{ n }-2.png")

frame3 = frame2[frame2["Algoritmo"] != "Shift-And Exato"]

plt.clf()

plot3 = sns.barplot(x = frame3["Tamanho"], y = frame3["Tempo"], hue=frame3["Algoritmo"]).get_figure()
plot3.savefig(f"figuras/figura{ n }-3.png")