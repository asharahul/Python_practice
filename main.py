#Tuple
tup1= (18, 18.09,"Hello",[97,99],{2,21},{1:"Hello", 2:"Hello"})
print(tup1)

tup1=(25,45,89,36,41,23,65,47,45,65,91,86,60)
print(tup1[3:7])
print(tup1[-1:-6:-1])

# len()----gives lenght of tuple
tup1=(45,32,56,578,96,58,6965,85,79,89)
a=len(tup1)
print(a)

# min()---gives minimum value of a tuple
tup1=(22,35,26,375,33,58,2,85)
a=min(tup1)
print(a)

tup1=("Hello","Dict","appkle","world")
a=min(tup1)
print(a)

# max()---gives maximum value of a tuple
tup1=(22,35,26,375,33,58,2,85)
a=max(tup1)
print(a)

# tuple(iterable)
tup1=tuple(range(100,125,4))
tup1=tuple("hrjkiuf jhr")
tup1=tuple([45,25,36,58])
tup1=tuple({45,58,96,58,74,5})
tup1=tuple({1:"Hello","wow":"great"})
print(tup1)


# index(element)---gives index of first occurence of element
tup1=(45,87,96,58,41,23,45,65,25,63)
tup1.index(45)
# tup1.index(45874)

#Set

Set1 = {35, 36, 33, 45, 55, 46, 67}
print(type(Set1))

Set1 = {35, 36, 33, 45, 55, 46,67 , 36, 35, 45, 35}
print(Set1)

t1 ={1,2,3,4,5,6,1,2,3}
print(t1)
print(type(t1))

set1={45,25,63,25}
set1.add("RahulB")
print(set1)

set1={45,25,63,25}
set1.add("xyz")
print(set1)

set1={45,65,87,45,8}
set1.clear()
print(set1)

set1={45,25,65,87,8}
set1.pop()
print(set1)

set1={45,65,87,458,45,87,45,98,54,56,36}
print(set1)
set1.remove(45)
print(set1)

s2 = set(range(12,20))
print(s2)
s2.remove(17)
print(s2)

set1={45,25,41,25,48,75,96,8}
set2={"hello","world"}
set3=set1.union(set2)
print(set1)
print(set2)
print(set3)

s6 = set(range(25,50))
s7 = {3,4,45,49,38,56, 57,67}
print(s6)
print(s7)
s8 = s6.intersection(s7)
print(s8)

set1={45,25,45,65,25}
set2={45,36,58,978}
print(set1.intersection(set2))

a = {45,67,89,90,92} ## it will remove the common values from your sets
b = {45,67,90,91}
a.difference_update(b)
print(a)

a={45,25,45,869,45}
a.discard(869)
print(a)

a={1,2,3,4,5}
b={6,7,8,9}
c=a.isdisjoint(b)
print(c)

a = set(range(1,6))
b = set(range(7,10))
c = a.isdisjoint(b) ## if condition is fuulfling then false other true
print(c)

a={45,25,36,58}
a.update(range(4,10))
print(a)
