# 1)Vypište prvních 5 členů posloupnosti:
# An = 2n - 1
x = 5
n = 1
for y in x:
	n = 2*n -1

# 2a)Vypište diferenci, víte-li, že a1=52 , a2=49.
a1 = int(52)
a2 = int(49)
d = a2 - a1
print(d)

# 2b)Vypište 30. člen této posloupnosti. 
a30 = a1 - d * 29
print(a30)
# 2c)Vypište součet a50 této posloupnosti.
a50 = a1 - d * 49
print(a50)

# 3)Je dán třicátý člen aritmetické posloupnosti a30=100 a diference d = 3. Kolikátým členem posloupnosti je číslo 280?
a30 = 100
d  = 3

while a30 == 280:
	n280 = a30 + d

# 4)Fibonacciho posloupnost
def fib2(num):
	a, b = 1, 1
	for _ in range(num - 1):
		a, b = b, a + b
	return a

print(fib2(10))