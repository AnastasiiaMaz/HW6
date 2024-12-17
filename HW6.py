def split_list(lst):#функция вызова списка и разделения списка
    first = lst[:(len(lst) + 1) // 2],# первый список
    second = lst[(len(lst) + 1) // 2:]# второй список
    return [first, second] #возвращает результат работы

# Поверка примеров
print(split_list([1, 2, 3, 4, 5, 6]))  # [[1, 2, 3], [4, 5, 6]]
print(split_list([1, 2, 3]))           # [[1, 2], [3]]
print(split_list([1, 2, 3, 4, 5]))     # [[1, 2, 3], [4, 5]]
print(split_list([1]))                 # [[1], []]
print(split_list([]))                  # [[], []]

