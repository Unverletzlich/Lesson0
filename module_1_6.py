set_ = {'Alex': 1987, 'Vladimir': 1980, 'Gleb': 2000, 'Ivan': 1974}
my_dict = set_
print(my_dict)
print(my_dict['Vladimir'])
print(my_dict.get('Denis', 'Отсутствует'))
my_dict.update({'Anton': 1988, 'Anastasiya': 2001})
a = my_dict.pop('Gleb')
print(a)
print(my_dict)

set_0 = {11, 2, 3, 3, 11, 5, 'string', True, False, (1, 3, 2), True}
my_set = set_0
print(my_set)
my_set.add(7)
my_set.add('integer')
my_set.discard('string')
print(my_set)
