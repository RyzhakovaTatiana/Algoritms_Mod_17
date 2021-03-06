array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

def qsort(array, left, right):
    middle = (left+right) // 2#делим последовательность пополам

    p = array[middle]#Путь р это середина последовательности чисел (массива)
    i, j = left, right# i это левые элементы, а j это правые элементы

    while i <= j:#пока элементы из левой части меньше или равны элементам из правой части
        while array[i] < p:#пока элементы массива из левой части меньше середины
             i += 1#переходить к следующему элементу левой части (от 0го индекса к первому и т.д.)

        while array[j] > p:#пока элемент из правой части массива больше центрального элемента (середины)
             j -= 1# потому что j это самый правый элемент (т.е. последний) и от него двигаться надо справа налево
             #от последнего элемента к предпоследнему и т.д. до середины
        if i <= j:#сравниваем самый левый элемент и самый правый.
            #Если элемент из левой части меньше, чем элемент из правой части
            array[i], array[j] = array[i], array[j]
            i += 1
            j += 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


a = qsort(array, left= 0, right=9)
print(a)


