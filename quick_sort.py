# -*- coding: utf-8 -*-

import random

def quick_sort(array):
    if(len(array) < 2):
        return array
    else:
        # 取数组的首位作为基准值
        pivot = array[0]
        # 小于等于基准值的数值放入less数组
        less = [i for i in array[1:] if i <= pivot]
        # 大于基准值的数值放入greater数组
        greater = [i for i in array[1:] if i > pivot]
        # 进行递归
        return quick_sort(less) + [pivot] + quick_sort(greater)

def generate_radom_array(num):
    array = []
    for i in range(num):
        array.append(random.randint(1, 100))

    return array

def test():
    origin_array = generate_radom_array(10)
    print(origin_array)

    sorted_array = quick_sort(origin_array)
    print(sorted_array)

if __name__ == '__main__':
    test()
