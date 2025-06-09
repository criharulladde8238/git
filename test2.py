def transform_rps_values_to_int(my_list):
    """
    Преобразует все элементы списка к типу int.
    :param my_list: Список с элементами (числа или строки).
    :return: Список с целочисленными значениями.
    """
    return [int(i) for i in my_list]


def add_rps_values_from_input():
    """
    Функция позволяет пользователю добавить новые значения RPS или указать срез текущего списка.
    Возвращает обработанный список значений RPS.
    """
    rps_values = [1000, '1500', 1300, '1400', 1000, 2000, 1500]
    copy_rps_values = transform_rps_values_to_int(rps_values)

    print("Введите значение RPS для добавления (через запятую) или срез списка в формате [start,end]")
    print("Например: 1600 или 1600,1700 или [1,3]")

    while True:
        user_input = input().strip()

        if not user_input:
            print("Анализ завершён.")
            break

        # Обработка среза
        if user_input.startswith("[") and user_input.endswith("]"):
            try:
                slice_str = user_input[1:-1].split(",")
                start = int(slice_str[0]) if slice_str[0] else None
                end = int(slice_str[1]) if len(slice_str) > 1 and slice_str[1] else None
                copy_rps_values = copy_rps_values[start:end]
                print(f"Срез применён: {copy_rps_values}")
                break

            except (ValueError, IndexError):
                print("Ошибка: Некорректный формат среза. Пример: [1,3]")

        # Обработка чисел или списка чисел
        elif "," in user_input:
            parts = user_input.split(",")
            if all(part.isdigit() for part in parts):
                copy_rps_values.extend(int(part) for part in parts)
                print("Значения добавлены.")
            else:
                print("Ошибка: Допустимы только числа.")

        # Обработка одного числа
        elif user_input.isdigit():
            copy_rps_values.append(int(user_input))
            print("Значение добавлено.")

        else:
            print("Ошибка: Неверный ввод. Можно ввести число, список или срез.")

    return copy_rps_values


def get_list_sum_value(lst):
    """
    Возвращает сумму элементов списка.
    """
    return sum(lst)


def get_list_average_value(lst):
    """
    Возвращает среднее значение списка.
    """
    return get_list_sum_value(lst) // len(lst) if lst else 0


def median_list_value(lst):
    """
    Возвращает медианное значение списка.
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) // 2
    else:
        return sorted_lst[mid]


def analise_list_tendencies(lst):
    """
    Анализирует тенденции: скачки, снижения или стабильность нагрузки.
    """
    median = median_list_value(lst)
    average = get_list_average_value(lst)

    lower_bound = median * 0.75
    upper_bound = median * 1.25

    if average < lower_bound:
        return "Происходят снижения"
    elif average > upper_bound:
        return "Происходят скачки"
    else:
        return "Нагрузка стабильна"


def get_how_often_repeat_values_in_list(lst):
    """
    Возвращает словарь: {значение: частота встречаемости}.
    """
    freq = {}
    for val in set(lst):  # Используем set для уникальности
        freq[val] = lst.count(val)
    return freq


def main():
    """
    Основная функция программы.
    """
    processed_list = add_rps_values_from_input()
    list_sum = get_list_sum_value(processed_list)
    list_avg = get_list_average_value(processed_list)
    list_median = median_list_value(processed_list)
    tendency = analise_list_tendencies(processed_list)
    frequency = get_how_often_repeat_values_in_list(processed_list)

    print(f"\nТекущий список: {processed_list}")
    print(f"Сумма всех значений: {list_sum}")
    print(f"Среднее значение: {list_avg}")
    print(f"Медианное значение: {list_median}")
    print(f"Анализ тенденций: {tendency}")
    print(f"Частота значений: {frequency}")


if __name__ == "__main__":
    main()
