def determinarvacunaJDCH():
  #Definir variables y otros 
  edad=0
  sexo=""
  vacuna=""
  mujer=1
  hombre=2
  #datos de entrada
  edad=int(input("ingresa la edad:"))
  sexo=int(input("ingrese el sexo:"))
  #proceso
  if edad>70:
    vacuna="C"
  elif edad<16:
    vacuna="A"
  elif sexo==1:
    vacuna="B"
  elif sexo==2:
    vacuna="A"
  #Datos de salida
  print("te corresponde la vacuna:",vacuna)

determinarvacunaJDCH()

#solicitar dos numeros y calcular la suma, resta, multiplicacion y division.
print("ingrese el primer numero:")
n1=float(input())
print("ingrese 1 segundo numero:")
n2=float(input())
suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2
print("la suma es:",suma)
print("la resta es:",resta)
print("la multiplicacion es:",mult)
print("la division es:",div)


  import os

puntos = float (input ('Ingresa el valor de puntos: '))
salario_minimo = float (input ('Ingresa el valor de salario minimo: '))
bono=0
if puntos<=100:
    bono=salario_minimo
if puntos>100 and puntos<=150:
    bono=salario_minimo*2
if puntos>150:
    bono=salario_minimo*3
print ('Valor de bono: ' + repr (bono))
print ()  


