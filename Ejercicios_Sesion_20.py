"""
#Funciones que ayudan a los ciclos break
while 1:
  num = int(input("Ingrese un número: "))
  print("Usted ingresó: ")
  if num < 0:
    break
print("Salió del programa)
"""

#Uso del break
print()
LoginOri = "Erick"
PassOri = "EC"
Intentos = 3
print()
print("Solo tienes tres intentos",Intentos, "intentos-\n")
Usuario = input("Dame el usuario: ")
Pssw = input("Dame la contraseña: ")
Intentos = Intentos - 1
print()
print()
while (Usuario != LoginOri or Pssw != PassOri) and Intentos > 0:
  print("Datos de usuario o contraseña inválidos. Intentar de nuevo")
  print("Te quedan",Intentos,"intentos")
  Inttentos = Intentos - 1
  Usuario = input("Dame el usuario: ")
  Pssw = input("Dame la contraseña: ")
  print()
  print()
  if Usuario == LoginOri and Pssw == PassOri:
    print("Datos correctos. Bienvenido")
  else:
    print("Intentos terminados. Cambia tu password")
