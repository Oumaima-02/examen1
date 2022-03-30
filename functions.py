import csv
'''
def read_csv():
    with open('files/Consum.csv') as csvfile:
        read_csv= csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            print(row[5:7:1])
'''
def read_csv():
    suma=0
    with open('files/Consum.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row  in read_csv:
            if row[5] == '3':
                suma= suma+1
        total=suma*3
        print('El total de Codi_Sector es: ', total)

