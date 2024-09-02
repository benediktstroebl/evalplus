from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_list = numbers.split()
    sorted_list = []
    for i in range(len(number_list)):
        if number_list[i] == 'zero':
            sorted_list.append('zero')
        elif number_list[i] == 'one':
            sorted_list.append('one')
        elif number_list[i] == 'two':
            sorted_list.append('two')
        elif number_list[i] == 'three':
            sorted_list.append('three')
        elif number_list[i] == 'four':
            sorted_list.append('four')
        elif number_list[i] == 'five':
            sorted_list.append('five')
        elif number_list[i] == 'six':
            sorted_list.append('six')
        elif number_list[i] == 'seven':
            sorted_list.append('seven')
        elif number_list[i] == 'eight':
            sorted_list.append('eight')
        else:
            sorted_list.append('nine')
    return " ".join(sorted_list)

