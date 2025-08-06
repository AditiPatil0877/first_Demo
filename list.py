list=[10,77,55,99,"Aditi","Hello"]
# print(list)
# [10, 77, 55, 99, 'Aditi', 'Hello']



list[0]=20
print(list,type(list))
# [20, 77, 55, 99, 'Aditi', 'Hello'] <class 'list'>

print(len(list))
# 6

list.append(10)
print(list)
#[20, 77, 55, 99, 'Aditi', 'Hello', 10]

list.extend([50,30,40])
print(list)
#[20, 77, 55, 99, 'Aditi', 'Hello', 10, 50, 30, 40]

list.insert(1,88)
print(list)
#[20, 88, 77, 55, 99, 'Aditi', 'Hello', 10, 50, 30, 40]

print(list.index(99))
#4

list.remove(88)
print(list)
#[20, 77, 55, 99, 'Aditi', 'Hello', 10, 50, 30, 40]

list.pop(9)
print(list)
#[20, 77, 55, 99, 'Aditi', 'Hello', 10, 50, 30]

list.reverse()
print(list)
#[30, 50, 10, 'Hello', 'Aditi', 99, 55, 77, 20]

list1=list.copy()
print(list1)
#[30, 50, 10, 'Hello', 'Aditi', 99, 55, 77, 20]

print(list.count(50))
#1
print(list1[1:7])
#[50, 10, 'Hello', 'Aditi', 99, 55]

