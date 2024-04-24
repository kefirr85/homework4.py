immutable_var = 1, 2, 3, 'Apple', "b"
print(immutable_var)
# Если пробовать изменять элементы кортежа таким образом "immutable_var[0] = 5" то программа выдает ошибку,
# так-как сами элементы в кортеже изменять нельзя, а вот если сделать в нутри корежа списки то тогда в нутри
# списков можно будет изменять элементы
immutable_var = ([1, 2, 3], ['Apple'], ["b"])
immutable_var[0][2] = 300
print(immutable_var)
immutable_var[1][0] = 'Яблоко'
print(immutable_var)
immutable_var[2][0] = 'CV'
print(immutable_var)

mutable_list = ([1,2,3], ['a'], ['b'], ['Data'])
print(mutable_list)
mutable_list[0][1] = 55
print(mutable_list)