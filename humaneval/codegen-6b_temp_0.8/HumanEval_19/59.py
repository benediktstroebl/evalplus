from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    new_list = []
    for i in range(0, 10):
        new_list.append(numbers.count(str(i)))
    # print(new_list)
    max_num = max(new_list)
    # print(max_num)
    for i in range(0, 9):
        if new_list[i] == max_num:
            new_list[i] = 0
            max_num -= 1
    # print(new_list)
    new_list.sort()
    # print(new_list)
    for i in range(0, 9):
        new_numbers = numbers.replace(str(i), "")
    return new_numbers

