from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split()
    for i in range(len(numbers_list)):
        if i == 0:
            continue
        for j in range(i, 0, -1):
            if int(numbers_list[j]) > int(numbers_list[j-1]):
                temp = numbers_list[j-1]
                numbers_list[j-1] = numbers_list[j]
                numbers_list[j] = temp
    return ' '.join(numbers_list)

