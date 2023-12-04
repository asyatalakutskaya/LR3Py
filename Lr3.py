import math
 
def functionSch(a, b, h, m):
    i=1
    x = a
    print('№', 'x', 'f(x)', sep='\t')
    while(x<=b):
        result = x**3-m*math.sin(x)
        print(i, round(x,3), round(result,3), sep='\t')
        i+=1
        x+=h

print("Введите значение a: ")
a = input()
print("Введите значение b: ")
b = input()
print("Введите значение h: ")
h = input()
print("Введите значение m: ")
m = input()
functionSch(float(a), float(b), float(h), float(m))