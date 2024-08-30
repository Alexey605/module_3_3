def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(2, 23, 33)
print_params('Hello', True, 44)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [12, 'Yes', 5.2]
values_dict = {'a':2.5, 'b':5, 'c':'Hello'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
