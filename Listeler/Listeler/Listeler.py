l=[]
for x in range (1,11):
    l.append(x**2)
print(l)
print(x)
squares =list(map (lambda y: y**2, range(10)))
print(squares)
#print (y)
def f(x):
    return x+5
l2=[2,3,4,5]
print(list(map(lambda x:x+5, l2)))
l3=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(l3)
