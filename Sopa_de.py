import random
import time

opcion = ['Sí.', 'No.', 'Es irrelevante.']
print("Un hombre pidió sopa de tortuga en un restaurante con vista al mar. El hombre tomó un sorbo de sopa,")
print("confirmó que era auténtica sopa de tortuga, pagó la cuenta, se fue a casa y luego se suicidó. ¿Por qué?")
time.sleep(2)
print('=========')
print("Cómo jugar: Ingrese su pregunta durante cada turno. La computadora responderá con 'Sí' o 'No' o 'Es irrelevante'.")
print("Cuando encuentre la solución a la historia, envíe una 'S' para terminar.")

while True:
    time.sleep(2)
    print('=========')
    x = input('La pregunta: ')
    time.sleep(2)
    if x == 'S':
        x = input('Ingrese la historia: ')
        break
    else:
        y = random.choice(opcion)
        print(y)
print('=========')
print(x)
time.sleep(100)