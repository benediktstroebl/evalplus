from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    pass
    numbers_list = [int(num) for num in numbers.split(' ')]
    sorted_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in numbers_list:
        sorted_numbers[num] += 1
    for i in range(len(sorted_numbers)):
        if i == 0:
            continue
        current_val = sorted_numbers[i]
        for j in range(current_val):
            sorted_numbers[i] += 1
            sorted_numbers[j] -= 1
    return ' '.join([str(num) for num in sorted_numbers])

