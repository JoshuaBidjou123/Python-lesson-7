# empty dictionary
my_dict ={1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict ={'name': 'John', 1: [2, 4, 3]}

my_dict ={'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])
print(my_dict.get('age'))

# update value
my_dict['age'] = 26
print(my_dict)

# remove particular element
print("Address:", my_dict.get('address'))

# remove all the elements
my_dict.clear()
print(my_dict)