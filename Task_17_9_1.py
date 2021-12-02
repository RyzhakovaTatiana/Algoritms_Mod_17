#Напишите программу, которой на вход подается последовательность
# чисел через пробел, а также запрашивается у пользователя любое число.

while True:
    try:
        my_array = list(map(int, input("Введите последовательность целых чисел через пробел: ").split()))
        num_by_person = int(input("Введите любое число, индекс которого будем искать в отсортированном списке: "))
        if num_by_person not in my_array:
            print("Введенного Вами числа нет в списке")


    # Если полученный ввод не число, будет вызвано исключение
    except ValueError:
        # Цикл будет повторяться до правильного ввода
        print("Вы ввели не целое число, попробуйте снова.")
        # При успешном преобразовании в целое число,
        # цикл закончится.
    else:
        break



#Функция сортировки списка по возрастанию элементов в нем
def my_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return (array)


print("Получился отсортированный список ", my_sort(my_array))
my_sorted_array = my_sort(my_array)

#Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу

def binary_search(array, element, left, right):
    if len(array) < 2:
        return "В списке недостаточно элементов для поиска. Введите больше чисел"
    if left > right:  # если левая граница превысила правую,
        return "Введенного Вами числа нет в списке"  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

# запускаем алгоритм на левой и правой границе
print("Индекс указанного Вами элемента в отсортированном массиве: ", binary_search(my_sorted_array, num_by_person, 0, len(my_sorted_array)))
