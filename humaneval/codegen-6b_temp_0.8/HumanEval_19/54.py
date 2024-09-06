from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = []
    for number in numbers.split():
        numbers_list.append(number_to_numeral[number])
    sorted_list = sorted(numbers_list)
    return ' '.join([numeral_to_number[i] for i in sorted_list])

