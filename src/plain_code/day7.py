# list类型
a = [1, 2, 3.0, '4', 5, 6, 7, 8, 9, 3.0, 10]

a.insert(3, 3.5)

for i in a:
    print(i)

a.remove(3.0)
a.pop(0)

for i in a:
    print(i)

a[4] = '5.1'
for i in a:
    print(i)

print(a.__contains__(10086))

for i in a:
    print(i)
