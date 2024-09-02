from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Check if numbers argument is not a string
    if not isinstance(numbers, str):
        raise TypeError('Input must be a string')
    # Split numbers into list
    number_list = numbers.split()
    # Check if number_list contains any values other than 'zero' - 'nine'
    for number in number_list:
        if number not in ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
            raise ValueError('Input must contain only "zero" - "nine"')
    # Sort the list
    number_list.sort()
    # Join the list to make a string
    return ' '.join(number_list)

