def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()

print_params(b=25)

print_params(c=[1, 2, 3])

print_params(10, 'пример строки', False)
values_list = [42, 'распакованная строка', False]
values_dict = {'a': 99, 'b': 'строка из словаря', 'c': [10, 20]}

print_params(*values_list)

print_params(**values_dict)
values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)