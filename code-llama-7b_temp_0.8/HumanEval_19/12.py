from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert string of numbers into a list of strings
    num_list = numbers.split()
    # Convert the list of strings into integers
    num_int_list = [int(s) for s in num_list]
    # Use sorted() and return the string of numbers
    return " ".join(map(str, sorted(num_int_list)))

