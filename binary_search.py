# -*- coding: utf-8 -*-

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        print(f"Search range: {low} - {high}")
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
    list = [n for n in range(1,20)]
    item = 13
    index = binary_search(list, item)
    if(index == None):
        print(f"{item} doesn't exist in list.")
    else:
        print(f"The index of {item} is {index}.")

if __name__ == '__main__':
    test()
