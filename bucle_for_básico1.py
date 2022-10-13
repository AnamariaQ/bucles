#1 Básico: imprime todos los números enteros del 0 al 150.
for d in range(151):
    print(d)

#2 Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
for e in range(5,1001,5):
    print(e)

#3 Contar, a la manera del Dojo: imprime números enteros del 1 al 100.
#Si es divisible por 5, imprime "Coding” en su lugar.
#Si es divisible por 10, imprime "Coding Dojo".'''
for a in range(101):
    if a%10 ==0:
        print("Coding Dojo")
    elif a%5 ==0:
        print("Coding")
    else:
        print(a)


#4 Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
g = 0
for m in range (500000):
    if m%2 ==1:
        g=g+m
    if m==499999:
        print(g)

#5 Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.

for f in range (2018,0,-4):
    print(f)

#6 Contador flexible: establece tres variables: lowNum, highNum, mult.
# Comenzando en lowNum y pasando por highNum, 
# imprime solo los enteros que sean múltiplos de mult.
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

lowNum = 10
highNum = 25
mult = 2

for num in range(lowNum, highNum, 1):
    if num%mult ==0:
        print(num)
#establezco las variables lowNum y highnum en un range para que se recorran los valores de 1 en 1
# luego divido la variable mult x range() para que me divida los valores y se imprima solo los numeros
#divisibles x 2.