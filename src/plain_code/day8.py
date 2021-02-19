# set类型
a = set()

a.add('hello')
a.add('nope')
a.add('hello')
print(a)

a.remove('hello')
print(a)

a = set('hello')  # a = {'hello'} 不能用a = {}来初始化空集合
b = set('world')
print(a, b)

print(a & b)
print(a | b)
c=set('hello world')
print(c - a)
