from funciones import *
from funciones2 import suma, agregarNumeroLista

def llamarSaludo():
  saludar()
  saludoPersonal('Federico')
  print(suma(2,5))

llamarSaludo()

lista = [2,5,6]

agregarNumeroLista(lista, 45)
print(lista)