from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    sort_numbers_list = []
    for index, char in enumerate(numbers):
        if index == 0:
            sort_numbers_list.append(char)
        else:
            if sort_numbers_list[-1] == char:
                sort_numbers_list.append(char)
            else:
                sort_numbers_list.append(char)
    return "".join(sort_numbers_list)

