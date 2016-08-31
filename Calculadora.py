
print("***************************")
print("*       CALCULADORA       *")
print("*          -By-           *")
print("*       ReaverZ3r0        *")
print("***************************")


def Suma(x,y):
    return x+y

def Resta(x,y):
    return x-y

def Multi(x,y):
    return x*y

def Division(x ,y):
    return x/y

def Resto(x ,y):
    return x%y


op = input("Introduce operacion(+,-,*,/,%): ")
var = int(input("Introduce enter primer numero: "))
var2 = int(input("Introduce enter segundo numero: "))
print("Resultado:")
if op == '+':
    print(Suma(var, var2))

elif op == '-':
    print(Resta(var, var2))

elif op == '*':
    print(Multi(var, var2))

elif op == '/':
    print(Division(var, var2))

elif op == '%':
    print(Resto(var, var2))