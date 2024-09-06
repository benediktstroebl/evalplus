from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # TODO: Sort numbers in order from smallest to largest
    number_list = numbers.split()
    for i in range(0, len(number_list)):
        number_list[i] = int(number_list[i][-1])

    return number_list.sort()

