#lst = [1,2,3,4,5,6,7]
#for x in lst:
#    if x == 5 :
#        continue
#    print(x)

#i = 0
#while i < len(lst):

#    i += 1
#    if i == 5 :
#        continue
#    print(i)
#while lst:
#    x = lst.pop(0)
#    print(x)
#else:
#    print("list mavjud emas !")

#for x in lst:
#    print(x)


def lst(*args):
    for x in args:
        return args[1]
#
print(lst(1,5,2,1))