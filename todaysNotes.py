# lists - ordered, mutable
# dictionaries - unordered collections, key-value pairs

#! list
fruits = ['apple','banana','grape']

#! dictionary
fruitColor = {'apple':'green','banana':'yellow','grape':'red'}


#? builtin list methods; append() remove() sort() pop() insert()
#! add item
fruits.append('orange')
print(fruits)
#! remove item
fruits.remove('banana')
print(fruits)
#! sort list (alphabetical order)
fruits.sort()
print(fruits)
#! nested list (list of lists; "multi-dimensional" dada storage)
multilist = [[1,2,3],[4,5,6],[7,8,9]]
print(multilist[1][1])
#* output is 5- first 1 is the second list, then second 1 is the second # in the list



# dictionary methods
# access key and value
keys = fruitColor.keys()
values = fruitColor.values()
print(keys)
print(values)

#! update dictionary
fruitColor['apple'] = 'yellow'
print(values)
#! get() for missing keys
print(fruitColor.get('orange', 'not found'))
#! add to dictionary
fruitColor.update({'tomato':'red'})
# or
fruitColor['peach'] = 'pink'