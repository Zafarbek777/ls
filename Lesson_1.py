import sys

# first program
print(sys.version)
print("hello world")
# command+/ kop qatorli comments
# izoh, comments

"""
verification qiladigan function 
"""
# 1
a = 12
print(4 * a)

# 12
a = 4
b = 3
c = (a**2+b**2)**(1/2)
p = a+b+c
print(p)

# 16

a = 5
b = 6

print(abs(a-b))


#17

a = 3
b = 5
с = 9

AC = abs(a-c)
BC = abs(b-c)

print(AC)
print(BC)
print(AC+BC)


x1 = 10
y1 = 12
x2 = 18
y2 = 22

result = ((x1-x2)**2+(y1-y2)**2)**1/2

print(result)


#21

x1 = 10
y1 = 12
x2 = 18
y2 = 22
x3 = 20
y3 = 11

a = ((x1-x2)**2+(y1-y2)**2)**1/2
b = ((x1-x3)**2+(y1-y3)**2)**1/2
c = ((x3-x2)**2+(y3-y2)**2)**1/2

p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**1/2



#25

x = float(input())
y = 3*(x**6)-6*(x**2)-7

print(y)

#27

A = float(input())
print(A**2, A**4, A**8)


#29

a = float(input())
r = a * (3.14/180)

print(r)















