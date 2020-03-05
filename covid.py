# import numpy as np

while True:
  try:
    # Me ingresan el nombre del fichero
    file_name = input('Ingrese el nombre del fichero: ')
    # Intento abrir el fichero
    f = open(file_name, 'r')
    # Lo guardo en una lista si funciona, sino se va en a la excepcion
    file_contents = f.readlines()
    # Cierro el archivo
    f.close()

    # Total de infectados
    total_infected = 13149 # len(file_contents)
    # Inicializo los contadores
    total_china = 0
    total_italy = 0
    total_japan = 0

    # Itero sobre los contenidos del archivo
    for country in file_contents:
      # Voy sumando al respectivo pais
      if country == 'China\n':
        total_china += 1
      elif country == 'Italy\n':
        total_italy += 1
      elif country == 'Japan\n':
        total_japan += 1

    # Abro el archivo
    estadisticas = open('estadisticas.txt', 'w')
    # Copio en el archivo
    estadisticas.write('El numero de infectados de China es de ' + str(total_china) + 
    ' y su porcentaje del total es de ' + str((total_china / total_infected) * 100) + '\n')
    estadisticas.write('El numero de infectados de Italy es de ' + str(total_italy) + 
    ' y su porcentaje del total es de ' + str((total_italy / total_infected) * 100) + '\n')
    estadisticas.write('El numero de infectados de Japan es de ' + str(total_japan) + 
    ' y su porcentaje del total es de ' + str((total_japan / total_infected) * 100) + '\n')
    # Cierro el archivo
    estadisticas.close()

    print('El total de infectados de China, Italy, y Japan es: ' + 
    str(total_china + total_italy + total_japan))

    # Si termino el programa salgo del while
    break
  except FileNotFoundError:
    print('Error: el fichero no existe')


