def transform_rps_values_to_int(my_list):
    """
    Функция преобразуется все значения списка к типу int
    :param my_list: передаваемый список
    :return: преобразованный список
    """
    my_new_list = []
    for i in my_list:  #copy_rps_values приводим все элементы списка к int
        my_new_list.append(int(i))
    my_list = my_new_list
    return my_list

def add_rps_values_from_input():
    slice_rps_list = []
    """
    Функция добавляет к списку новые значения RPS и может обозначить срез по текущему списку
    :return: возвращает список с введенными значениями\срез текущего списка
    """
    print("Введите значение RPS, чтобы добавить его к текущему списку (число или список чисел подряд через запятую)")
    print("Вместо анализа целого списка можно указать его срез пример ввода[1,3]")
    print("Где первая цифра отсекает количество объектов от начала списка")
    print("Вторая цифра отсекает n элемент и все что после него")
    rps_values = [1000, '1500', 1300, '1400', 1000, 2000, 1500]
    copy_rps_values = rps_values.copy()  # copy_rps_values используется для вывода изначального списка
    copy_rps_values = transform_rps_values_to_int(copy_rps_values)


    while True:
        input_rps_value = input()
        if input_rps_value.isdigit(): #Добавление элемента списка
            copy_rps_values.append(int(input_rps_value))
            print(f"Значение добавлено в список")
          #  return copy_rps_values
        elif "," in input_rps_value: #Добавление элементов списка пачкой через символ ","
            if "[" and "]" in input_rps_value: #Обозначение среза для текущего списка
                input_rps_value = input_rps_value.replace('[', '')
                input_rps_value = input_rps_value.replace(']', '')
                slice_rps_list.extend(input_rps_value.split(","))
                x, y = slice_rps_list
                if x == "":
                    print(f"Отсекаем все объекты после индекса {y} ")
                    copy_rps_values = copy_rps_values[:int(y)]
                    return copy_rps_values
                elif y == "":
                    print(f"Отсекаем {x} элементов от начала списка ")
                    copy_rps_values = copy_rps_values[int(x):]
                    return copy_rps_values
                else:
                    x, y = slice_rps_list
                    print(f"Отсекаем {x} элементов от начала списка, отсекаем все объекты после индекса {y} ")
                    copy_rps_values = copy_rps_values[int(x):int(y)]
                    return copy_rps_values
            else:
                print(f"Значения добавлены")
                copy_rps_values.extend(input_rps_value.split(","))
         #       return copy_rps_values

        elif input_rps_value == "":
            print(f"Результаты анализа:")
            copy_rps_values = transform_rps_values_to_int(copy_rps_values)
            return copy_rps_values
        else:
            print("Значение не добавлено, на ввод допустимы только числа")



def get_list_sum_value(copy_rps_values):
    """
    Функция получает сумму элементов списка
    :param copy_rps_values: список
    :return: сумма элементов списка
    """
    list_sum = 0
    for i in copy_rps_values:  # Вычисляем сумму всех элементов списка,а так же его среднее значение
        list_sum += i
    return int(list_sum)

def get_list_average_value(copy_rps_values):
   """
   Функция получает среднее значение списка
   :param copy_rps_values: список
   :return: среднее значение списка
   """
   list_size = len(copy_rps_values)
   list_sum = get_list_sum_value(copy_rps_values)
   list_average = list_sum // list_size
   return list_average

    # Вычисляем медианное значение списка
def median_list_value(copy_rps_values):
    """
    Функция вычисляет медианное значение списка
    :param copy_rps_values: список
    :return: медианное значение списка
    """
    list_size = len(copy_rps_values)
    quotient, remainder = divmod(list_size, 2)
    median = copy_rps_values[quotient] if remainder else sum(copy_rps_values[quotient - 1:quotient + 1]) / 2
    return int(median)

def analise_list_tendencies(copy_rps_values):
    """
    Функция вычисляет отклонения выше\ниже 25% в разнице между медианным и среднем значением списка
    если таковы есть, в любом другом случае значения считаются стабильными
    :param copy_rps_values: список
    :return: функция возвращает результат производимого анализа
    """
    median = median_list_value(copy_rps_values)
    list_average = get_list_average_value(copy_rps_values)
    median_75_percent_value = (median / 100) * 75
    median_125_percent_value = (median / 100) * 125
    if list_average > median_125_percent_value:
        analise = "Происходят скачки"
        return analise
    elif list_average < median_75_percent_value:
        analise = "Происходят снижения"
        return analise
    else:
        analise = "Нагрузка стабильна"
        return analise

def get_how_often_repeat_values_in_list(copy_rps_values):
    """
    Функция считает как часто встречается каждый объект в списке
    :param copy_rps_values: список
    :return: пара 'объект': 'частота в списке'
    """
    rps_values = copy_rps_values.copy()
    n = 0
    list_values = {}
    list_size = len(rps_values) - 1
    for i in copy_rps_values:
        while list_size > -1:
            if i == rps_values[list_size]:
                n += 1
                list_size = list_size - 1
                x = rps_values.pop()
                frequency_rps_value = {x: n}
            elif i != rps_values[list_size]:
                rps_values.pop()
                list_size = list_size - 1
        list_values.update(frequency_rps_value)
        rps_values = copy_rps_values.copy()
        n = 0
        list_size = len(rps_values) - 1
    return list_values

def main():

    copy_rps_values = add_rps_values_from_input()
    list_sum = get_list_sum_value(copy_rps_values)
    list_average = get_list_average_value(copy_rps_values)
    median = median_list_value(copy_rps_values)
    analise = analise_list_tendencies(copy_rps_values)
    frequency_rps_value = get_how_often_repeat_values_in_list(copy_rps_values)
    print(f"Текущий список {copy_rps_values}")
    print(f"Сумма всех значений {list_sum}")
    print(f"Среднее значение {list_average}")
    print(f"Медианное значение {median}")
    print(analise)
    print(f"(Объект : Встречается раз) {frequency_rps_value}")

main()
