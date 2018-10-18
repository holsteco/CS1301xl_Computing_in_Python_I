#corey b. holstege
#2018-10-18
#problem 2.4.10

a = 5
a **= 2
b = a % 5
a *= b
b += 5
a -= b
c = a == b
d = a**2 == b**2
e = c or d

print(a)
print(b)
print(c)
print(d)
print(e)