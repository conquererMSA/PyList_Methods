'''
What is List in Python: List is a collective data type to store
diffrent collection of data in a single variable.
List is not simillar to Array.
Array is store simillar type data in a single variable. On the
other hand list is used to store diffrent data type ina single
variable.
list=['name', 30, 45,3+j,true] diff data type
array=[20.30,56] simillar data type
'''

#list indexing
'''
list er single item access korar jonno indexing use kora hoy.
list1=[23,6+j7,'yes']
list er protity item er jonno duiti index ache:
1. positive indexing //firstItem=list1[0] =>23
2. negative indexing //firstItem=list[-3] =>23
and list er multiple item access korar jonno slicing use kora hoy.
'''
#concatenation of two list
l1=[34,55,75,43,True, 'Tsy']
l2=['MSA','Pvs',45.68,"name"]
l3=l1+l2
# print(id(l3)) #2251807580928
# print(id(l1))
# print(l3) # [34, 55, 75, 43, True, 'name', 'MSA', 'Pvs', 45.68, 'name']

#multiplication of a list
triple1=l1*3 # [34, 55, 75, 43, True, 'Tsy', 34, 55, 75, 43, True, 'Tsy', 34, 55, 75,
# 43, True, 'Tsy']
#ekahne l1 list er value gulu ekti notun list er moddhye tin bar kore takbe..
# print(triple1)

# Membership operator
'''
membership operator return boolean value True/False
membership operator check kore list er moddhye kuno item ache kina 
if/elif/else condition use kora zay
1. in 
2. not in
'''
if 'name' in l2:
    pass
    # print('Yes') //True
else:
    pass
    # print('No')

def findLength(anyList):
    count=0
    for item in anyList:
        count+=1
    return count
listLength=findLength(l1)
# print(listLength) //6
list2Length=len(l2)
# print(list2Length) //4

