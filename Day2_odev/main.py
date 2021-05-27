numbers=range(0,31)
list1=list()
list2=list()
for i in numbers:
    if(i%2==1):
        list1.append(i)
    else:
        list2.append(i)
mergedList= [i*2 for i in list1+list2] #list comprehension
mergedList.sort() #birleşitirilmis,2 ile çarpılmış ve sıralanmış yeni listemiz.
for i in mergedList:
    print("Value: {} Data type: {}".format(i,type(i)))

"""
istersek bu şekilde listeleri birleştirip 2 ile çarpabiliriz 
mergedlist=list()
for i in list1+list2:
    mergedlist.append(i*2)
mergedlist.sort()

"""