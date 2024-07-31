tuple_imut = 12, 23, 'Tuple', False
immutable_var = tuple_imut
print(immutable_var)
mutable_list = [12, 23, 'Tuple', False]
print(mutable_list)
mutable_list[0] *= 2
mutable_list[2] = 'List ' + 'Mutable'
print(mutable_list)
tuple_mut = ([1, 2, 3], [3, 2, 1])
print(tuple_mut)
mutable_var = tuple_mut
mutable_var[0][2] /= 5
mutable_var[1][0] *= 7
print(mutable_var)
