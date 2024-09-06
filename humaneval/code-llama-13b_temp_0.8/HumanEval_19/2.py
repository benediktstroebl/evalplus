from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split the string into list of numbers
    numbers = numbers.split()
    # create a list of tuples
    numbers = [(number, str(index)) for index, number in enumerate(numbers)]
    # sort the list of tuples
    numbers.sort(key=lambda x: x[0])
    # join the list of tuples into string
    return ' '.join([item[1] for item in numbers])

