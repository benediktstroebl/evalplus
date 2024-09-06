from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the string into list of numbers
    numbers_list = numbers.split()

    # Cast to int, sort, cast to string
    sorted_numbers = ' '.join(
        map(str, sorted(map(int, numbers_list)))
    )
    return sorted_numbers

