from copy import copy, deepcopy

# lst = [1, 2, 3, 4, 5]

# 1 1.0 "hello" True 

# lst_two = copy(lst)

# print(lst_two)

# my_list = [1, 2, 3]
# my_list_two = my_list

# my_list[1] = 9
# print(my_list_two)


lst = [[1, 2, 3], [4, 5, 6]]

# lst_two = copy(lst)
lst_two = deepcopy(lst)

lst[0][1] = 9

print(lst_two)