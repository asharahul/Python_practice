for x in "Rahul":
    print(x)

a = list(range(0,12,2))
print(a)

l1 = list(range(10,20,2))
for i in l1:
    if i == 14:
     continue
    print(i) 

l2 = ["Rahul", "Asha","Dhruvi"]
for x in l2:
    if x=="Asha":
      continue
    print(x)

l = [1,2,3,4]
for i in l:
    if i ==4:
        continue
    print(i)

l1 = [1,2,3,4,5,6]
for x in l1:
     if  x== 3:
          x += 1
          break
print(x)

l2 = list(range(26,50,2))
for a in l2:
    if a ==40:
        break
    print(a)

l1 = ["Rahul","Bobby","Shivang"]
for x in l1:
    if x=="Bobby":
     break
    print(x)

for x in range (15):
    print(x)

for x in range (6):
    if x == 7:
        break
    print(x)
else: 
  print("Finished")

for  x in range (5,10):
    if x == 9:
        break
    print(x)
else:
    print("finished")

adj = ["red", "Green", "Blue"]
fruits = ["Mango", "Banana", "Apple"]
for x in adj:
    for y in fruits:
        print(x,)

While Loop
x = 3
while x < 6:
    print(x)
    x += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

