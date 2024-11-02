#Задание "Раз, два, три, четыре, пять .... Это не всё?":
def calculate_structure_sum(data_structure):
    list_ = []
    for i in data_structure:
        bool = True
        if isinstance(i, int):#если целые числа
            bool = True
            list_.append(i)
        elif isinstance(i, str):#если строчные значения
            bool = True
            list_.append(len(i))
        elif isinstance(i, dict):#если словарь
            bool = True
            for j in i:
                if isinstance(j, int):#если в словаре ключ целое число
                    bool = True
                    list_.append(j)
                elif isinstance(j, str):#если в словаре ключ строка
                    bool = True
                    list_.append(len(j))
            for h in i.values():
                if isinstance(h, int):#если в словаре значение целое число
                    bool = True
                    list_.append(h)
                elif isinstance(h, str):#если в словаре значение строка
                    bool = True
                    list_.append(len(h))
        elif isinstance(i, (list, set, tuple)):#если список
            for item in i:
                bool = True
                list_.append(item)
    first_number = list_[0]#первое число для прибавления
    if len(list_) == 1:#точка для выхода рекурсии
        return first_number
    elif len(list_) >= 1:#что суммируем
        return first_number + calculate_structure_sum(list_[1:])#сложение
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)












