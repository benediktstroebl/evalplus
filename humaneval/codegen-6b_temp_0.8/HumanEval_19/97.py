from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    from string import digits

    number_map = {'one': '0', 'two': '1', 'three': '2', 'four': '3', 'five': '4', 'six': '5', 'seven': '6',
                  'eight': '7', 'nine': '8', 'ten': '9', 'zero': '0'}

    ordered_numbers = ''

    for number in numbers.split():
        ordered_numbers += number_map[number]

    return ordered_numbers

