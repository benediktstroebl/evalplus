from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    number_list: List[str] = [x for x in numbers.split(' ')]
    sorted_list: List[str] = []
    for num in number_list:
        if num == 'zero':
            sorted_list.append('zero')
        elif num == 'one':
            sorted_list.append('one')
        elif num == 'two':
            sorted_list.append('two')
        elif num == 'three':
            sorted_list.append('three')
        elif num == 'four':
            sorted_list.append('four')
        elif num == 'five':
            sorted_list.append('five')
        elif num == 'six':
            sorted_list.append('six')
        elif num == 'seven':
            sorted_list.append('seven')
        elif num == 'eight':
            sorted_list.append('eight')
        elif num == 'nine':
            sorted_list.append('nine')
    return " ".join(sorted_list)

