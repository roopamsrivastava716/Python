# List
List is a collection which is ordered and changeable.
Allows duplicate members.


list1= [10, 15.5 , 'Python', 'A',"abc"]
#        0   1          2      3    4  
len(list1)

list2 = ['xyz', 'ABC', 'XYZ']
type(list2)

print('list1=',list1)
print('list2=',list2)


print('type(list1)=',type(list1))

print('Length of list1 = ', len(list1))

print('=========================')
print('String slicing')
#Fist element = List1[0]
print('list1[0] = ',list1[0])
print('list1[1] = ',list1[1])
print('list1[2] =',list1[2])

# list[startindex : endIndex (excluding) : interval]
print('list1[2:5] = ',list1[2:5])   # ['Python', 'A', 'abc']

print('list1[0:2] = ',list1[0:3]) # [10, 10.5]

print('list1[::2] = ',list1[::2]) #[10, 'Python', 'abc']


# List Reverse without using function

print('List reverse list1[::-1]',list1[::-1])

##list.reverse()

listA=[2,3,4,4,66,54]
listA.reverse()
print('Reversed List= ',listA)

#Slicing using reverse indexing
list4=[1, 2, 3, 4, 5, 7]
#index -6 -5 -4 -3 -2 -1
#list4[0:4]
list4[-4:-1]

print('===========================')
print('List built-in methods')

print('max(list2)= ',max(list2))

print('min(list2)= ',min(list2))
print('===========================')

list3 = list1 + list2
print('list1 + list2 = ',list3)
print('list1=',list1)
print('list2=',list2)

print('list2*3=',list2*3)

# max work on homogesnous list, doesn`t work on nonhomogenous 
#TypeError: '>' not supported between instances of 'str' and 'int'
list4=[1,2,5,6,'b']
max(list4)

print('Python in list1 = ','Python' in list1)

print('Python in list1 = ',10 in list1)

print('Python in list2 = ','Python' in list2)

print('Python in list1 = ','Python' not in list1)

print('Python in list2 = ','Python' not in list2)

print('============================')

a,b=1,2

list1,list2= [10, 15.5 , 'Python', 'A',"abc"],['xyz', 'ABC', 'XYZ']

print("list1,list2= [10, 15.5 , 'Python', 'A','abc'],['xyz', 'ABC', 'XYZ']")
print('list1=',list1)
print('list2=',list2)

print('============================')
print('============================')

#method to add elements to the list

# list.append(element)
list2.append('Python')
print(list2) # ['xyz', 'ABC', 'XYZ', 'Python']
print('============================')

# list.extend(seq)
list2.extend('rv')
print(list2) # ['xyz', 'ABC', 'XYZ', 'Python', 'r', 'v']
print('============================')



# list.append(seq)
list1.append(list2)  # [10, 15.5, 'Python', 'A', 'abc', ['xyz', 'ABC', 'XYZ', 'Python', 'r', 'v']]
print(list1)
print('len(list1)',len(list1)) # 6

print('list1[5]',list1[5])    # ['xyz', 'ABC', 'XYZ', 'Python', 'r', 'v']

print('list1[5][0] = ',list1[5][0])     #xyz

print('============================')


# list.extend(seq)
list1.extend(list2)
print('list1=',list1)   # [10, 15.5, 'Python', 'A', 'abc', ['xyz', 'ABC', 'XYZ', 'Python', 'r', 'v'], 'xyz', 'ABC', 'XYZ', 'Python', 'r', 'v']
print('len(list1)',len(list1)) # 12


print('============================')
print('============================')

list3 = [10,20,30,40]
print('list2= ', list2)
print('list3= ', list3)
list2.extend(list3)
print('list2 = ',list2)   # list2 =  ['xyz', 'ABC', 'XYZ', 'Python', 'r', 'v', 10, 20, 30, 40]

# insert(index, element)

list2.insert(3,'epro')  # list2 =  ['xyz', 'ABC', 'XYZ', 'epro', 'Python', 'r', 'v', 10, 20, 30, 40]
print('list2 = ',list2)

print('============================')
print('============================')

# to check the index position of an element
#list.index(element)
print('list2.index("Python")=',list2.index('Python'))

print('============================')
print('len(list2) = ',len(list2))
list2.append('xyz')
list2.append('xyz')
list2.append(10)
print('list2',list2)
print('len(list2) = ',len(list2))

# to count the number of occurances
# list2.count(element)

print('list2.count("xyz") = ',list2.count('xyz'))
print('list2.count(10) = ',list2.count(10))
print('list2.count("Python") = ',list2.count('Python'))

print('============================')
print('============================')

# to remove the elements from the list
    # pop(index)
    # remove(element)

# list.remove(element)
print('list2',list2)
print('list2.count("xyz") = ',list2.count('xyz'))
list2.remove('xyz')
print("=========list2.remove('xyz')===============")
print('list2',list2)
print('list2.count("xyz") = ',list2.count('xyz'))
print('============================')

list2.pop()
print('list2 before pop()',list2)   # list2 ['ABC', 'XYZ', 'epro', 'Python', 'r', 'v', 10, 20, 30, 40, 'xyz', 'xyz']

list2.pop(2)
print('list2 after pop(2)',list2) # list2 after pop(2) ['ABC', 'XYZ', 'Python', 'r', 'v', 10, 20, 30, 40, 'xyz', 'xyz']

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
























