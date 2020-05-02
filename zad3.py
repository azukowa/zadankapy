import math
a = (float(input("first side: ")))
b = (float(input("second side: ")))
c = (float(input("third side: " )))
p = 0.5*(a+b+c)
f = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f)