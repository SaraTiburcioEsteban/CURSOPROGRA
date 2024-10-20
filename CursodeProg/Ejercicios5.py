import math
print("hola, te ayudaré a calcular la altura del edificio si el cateto adyacente mide 2 veces el lado del pentagono de tu imagen")
A=float(input("ingrese el área del pentágono: \n"))
a=float(input("ingrese el valor de la apotema: \n"))
P=2*A/a
L=P/5
C1=2*L
t=math.tan(38)
C2=t*C1
print("esta es la altura del edificio: \n", C2, "metros")
