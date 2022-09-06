import random

def run():
  vidas = 5
  numero_aleatorio = random.randint(1, 100)
  print('Vamos a jugar Adivina el numero, solo tienes ' + str(vidas) + ' vidas')
  numero_elegido = int(input('Elige un numero del 1 al 100: '))

  while numero_elegido != numero_aleatorio and vidas > 0:
    if numero_elegido < numero_aleatorio:
      vidas -= 1
      if vidas > 0:
        print('Solo te quedan ' + str(vidas) + ' vidas')
      else:
        print('OK un ultimo intento')
      print('Elige un numero mas grande')
      numero_elegido = int(input('Elige otro numero: '))
    else:
      vidas -= 1
      if vidas > 0:
        print('Solo te quedan ' + str(vidas) + ' vidas')
      else:
        print('Ultimo intento')
      print('Elige un numero mas pequeño')
      numero_elegido = int(input('Elige otro numero: '))
  if vidas > 0:
    print('Ganaste!')
  else:
    print('Perdiste')

if __name__ == '__main__':
  run()
