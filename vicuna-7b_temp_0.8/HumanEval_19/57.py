from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    sorted_numbers = []
    for number in numbers:
        try:
            number_int = int(number)
            sorted_numbers.append(number_int)
        except ValueError:
            pass
    return sorted_numbers

