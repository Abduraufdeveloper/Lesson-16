lst = [1,2,3,4,5,6,7]
for x in lst:
    if x == 5 :
        continue
    print(x)

i = 0
while i < len(lst):

    i += 1
    if i == 5 :
        continue
    print(i)
while lst:
    x = lst.pop(0)
    print(x)
else:
    print("list mavjud emas !")

for x in lst:
    print(x)


def lst(*args):
    for x in args:
        return args[1]
#
print(lst(1,5,2,1))


def lst(**kwargs):
    for x in kwargs:
        print(x,kwargs[x])



#def numer(num):
 #   x = 12

#print(numer())

def s(n = 1 ,m = 2):
    return n + m
print(s(3,5))


def lst1():
    pass
lst1()
a = 12
def lst2():
    return a + 4
print(lst2())




num = input()
def lst3():
    global num
    num =[1,2,3,4,5,6]
    return num
print(lst3())


for x in num:
    print(x)



func = lambda x:x ** 2
print(func(2))
