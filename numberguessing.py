# empty dictionary
my_dict ={1: 'apple', 2: 'ball'}

# dictionary with mixed keys

my_dict ={'name': 'Jack', 'age': 12, 1: [8, 10, 23]}

# Output: Jack
print(my_dict['name'])
print(my_dict.get('age'))

# update value
my_dict['age'] = 12
print(my_dict)

# remove particular element
print("Address:", my_dict.get('address'))

# remove all the elements
my_dict.clear()
print(my_dict)