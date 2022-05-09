def saludo(mensaje):
    print(mensaje)
    
saludo("Hola Marina") #Llamando a la función saludo
saludo("Hola Carlos")

def suma(a,b,c): # a y b son los parametros de la función 
    print(type(a))
    return a+b+c
a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))
print(suma(a,b,c))# a y b son los argumentos de la función 

def resta(n1,n2):
    c = n1-n2
    d = n2-n1
    return c,d
print(resta(9,7))







   
    