def calcular_descuento(sexo, nacimiento):
  # Calculo la edad
  edad = 2020 - nacimiento
  # Variable donde guardo el valor del descuento
  descuento = 0

  # Si es 'H' calculo descuentos de hombre
  if sexo == 'H':
    # Condiciones según edad.
    if edad < 18:
      descuento = 5
    elif edad <= 30:
      descuento = 10
    elif edad <= 50:
      descuento = 20
    else:
      40
  # Si no es 'H' es 'M' porque cuando leimos verificamos 
  # y calculo descuetos.
  else:
    # Condiciones según edad.
    if edad < 18:
      descuento = 10
    elif edad <= 30:
      descuento = 20
    elif edad <= 50:
      descuento = 30
    else:
      descuento = 50

  return descuento


# Pregunto el número de usuarios.
n = int(input('Ingrese el numero de usuarios: '))
# Inilicializo mi diccionario de usuarios.
usuarios = {}

# Ciclo para preguntar 'n' veces
for i in range(n):
  # Valores iniciales para entrar a los 'while' cada que pregunte.
  sexo = ''
  nacimiento = 0

  # Pregunto el sexo hasta que esté bien.
  while sexo != 'H' and sexo != 'M':
    sexo = input('Ingrese su sexo: ')

  # Pregunto año de nacimiento hasta que esté bien.
  while nacimiento < 1920 or nacimiento > 2020:
    nacimiento = int(input('Ingrese su año de nacimiento: '))

  # Agrego usuario al diccionario
  usuarios[i] = [sexo, nacimiento]

# Itero sobre el diccionario
for _, v in usuarios.items():
  # Accedo a los valores de la lista '[sexo, nacimiento]' con v[0] y v[1]
  # e invoco la función 'calcular_descuento' con estos valores.
  print(f'El descuento es: {calcular_descuento(v[0], v[1])}')

