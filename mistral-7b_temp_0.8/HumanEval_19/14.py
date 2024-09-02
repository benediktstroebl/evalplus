from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Write your code here.

    # TODO: write your code here

    """
    First create a list of all digits, use the function `list.split()`
    Split the string on the space `' '`.
    Then sort the list.
    Return the string from the sorted list.
    """
    result = list()
    numbers = numbers.split()
    for digit in numbers:
        digit = digit.lower()
        result.append(digit)
    result.sort()
    return ' '.join(result)

