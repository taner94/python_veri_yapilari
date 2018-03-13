from collections import deque
l=[1,2,3]
l.append(55)
print (l)
print(l.pop())
print (l)
print(l.pop())
print (l)
l2=[44,55,66]
l2.append(77)
print(l2.pop(0))
print(l2)
l3 =deque([11,22,34,55])
print(l3)
l3.append(67)
print(l3.popleft())
print(l3)
