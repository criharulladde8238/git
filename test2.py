#Исходные данные
rps_values = [1000, '1500', 1300, '1400', 1000, 2000, 1500]
copy_rps_values = rps_values.copy() #copy_rps_values используется для вывода изначального списка
copy_rps_values = [int(i) for i in copy_rps_values] #copy_rps_values приводим все элементы списка к int
slice_rps_list = []

#Здесь начинается ввод данных
while True:
    print("Введите значение RPS, чтобы добавить его к текущему списку (число или список чисел подряд через запятую)")
    print("Вместо анализа целого списка можно указать его срез пример ввода[1,3]")
    print("Где первая цифра отсекает количество объектов от начала списка")
    print("Вторая цифра отсекает n элемент и все что после него")
    input_rps_value = input()
    if input_rps_value.isdigit(): #Добавление элемента списка
        rps_values.append(int(input_rps_value))
        print(f"Значение добавлено в список")
    elif "," in input_rps_value: #Добавление элементов списка пачкой через символ ","
        if "[" and "]" in input_rps_value: #Обозначение среза для текущего списка
            input_rps_value = input_rps_value.replace('[', '')
            input_rps_value = input_rps_value.replace(']', '')
            slice_rps_list.extend(input_rps_value.split(","))
            x, y = slice_rps_list
            if x == "":
                print(f"Отсекаем все объекты после индекса {y} ")
                rps_values = rps_values[:int(y)]
                break
            elif y == "":
                print(f"Отсекаем {x} элементов от начала списка ")
                rps_values = rps_values[int(x):]
                break
            else:
                x, y = slice_rps_list
                print(f"Отсекаем {x} элементов от начала списка, отсекаем все объекты после индекса {y} ")
                rps_values = rps_values[int(x):int(y)]
                break
        else:
            # noinspection PyTypeChecker
            rps_values.extend(input_rps_value.split(","))
            print(f"Значения добавлены")
    elif input_rps_value == "":
        print(f"Результаты анализа:")
        break
    else:
        print("Значение не добавлено, на ввод допустимы только числа")

int_rps_values = [int(i) for i in rps_values]
list_sum = 0
list_size = len(int_rps_values)
for i in int_rps_values: #Вычисляем сумму всех элементов списка,а так же его среднее значение
    list_sum += i
list_average_value = list_sum // list_size
quotient, remainder = divmod(list_size, 2)

#Вычисляем медианное значение списка
median = int_rps_values[quotient] if remainder else sum(int_rps_values[quotient - 1:quotient + 1]) / 2

print(f"Изначальный список {copy_rps_values}")
print(f"Текущий список     {int_rps_values}")
print(f"Сумма всех значений списка {list_sum}, количество элементов {list_size}, среднее значение {list_average_value}, Медианное значение {median}")
print()
##Если среднее сильно ниже медианы - были снижения
##При четном количестве элементов в списке, медиана будет равняться среднему значению двух элементов по соседству(по середине)
#
#
median_75_percent_value = (median / 100) * 75
median_125_percent_value = (median / 100) * 125
if list_average_value > median_125_percent_value:
    print("Происходят скачки")
elif list_average_value < median_75_percent_value:
    print("Происходят снижения")
else:
    print("Нагрузка стабильна")
rps_values_copy = int_rps_values.copy()
n = 0
list_values = {}
list_size = len(rps_values_copy) - 1

#Вычисляем как часто встречаюся одинаковые элементы списка
for i in int_rps_values:
    while list_size > -1:
        if i == rps_values_copy[list_size]:
            n += 1
            x = rps_values_copy.pop()
            list_size = len(rps_values_copy) - 1
            frequency_rps_value = {x: n}
        elif i != rps_values_copy[list_size]:
            rps_values_copy.pop()
            list_size = len(rps_values_copy) - 1
    list_values.update(frequency_rps_value)
    rps_values_copy = int_rps_values.copy()
    n = 0
    list_size = len(rps_values_copy) - 1
print("Значение : Встречается раз")
for k, v in list_values.items():
    print(k, v, sep=":")