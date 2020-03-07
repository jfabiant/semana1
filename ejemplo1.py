import pandas as pd
import numpy as np

# reading the file with the data
df = pd.read_csv("./dataSet/medallero_Panamericanos_Lima2019.csv")

# print the data in console
# print(df)


def calc_suma():
    print("Firt form ")
    print(df['Oro'].sum())
    print(df.Oro.sum())
    print("Second form ")
    print(np.sum(df['Oro']))
    print(np.sum(df.Oro))


def calc_nro_elementos():
    print("Firt form ")
    print(len(df['Oro']))
    print(len(df.Oro))
    print("Second form")
    print(df['Oro'].count())
    print(df.Oro.count())
    print("Third form")
    print(np.size(df['Oro']))
    print(np.size(df.Oro))

def calc_media(redondeo = 2):
    media = df.Oro.mean()
    media = round(media, redondeo)
    return media

if __name__ == '__main__':
    print("CALCULANDO LA SUMA")
    calc_suma()
    print("CALCULANDO EL NUMERO DE ELEMENTOS")
    calc_nro_elementos()
    print("HALLANDO LA MEDIA DEL ATRIBUTO ORO")
    print(calc_media(4))