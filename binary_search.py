# -*- coding: utf-8 -*-

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = (low + high) // 2
        guess = list[mid]
        if(guess == item):
            return mid
        if(guess > item):
            high = mid - 1
        else:
            low = mid + 1

    # Reutrn None if item not found
    return None

def test():
    list = [1, 3, 5, 7, 9]
    item = 1
    index = binary_search(list, item)
    print(f"The index of {item} is {index}")

if __name__ == '__main__':
    test()
