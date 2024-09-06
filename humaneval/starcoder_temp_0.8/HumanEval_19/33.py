from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the numbers into a list of strings
    numbers_list = numbers.split()

    # Cast the strings to int
    numbers_list = [int(num) for num in numbers_list]

    # Sort the list
    numbers_list.sort()

    # Return the sorted list as a space-delimited string
    return''.join(map(str, numbers_list))

