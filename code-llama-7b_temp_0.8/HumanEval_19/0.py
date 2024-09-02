from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_list = numbers.split(' ')
    for i in range(len(number_list)):
        for j in range(len(number_list) - 1):
            if number_list[j] > number_list[j+1]:
                number_list[j] = number_list[j+1]
                number_list[j+1] = number_list[j]
    return ' '.join(number_list)

