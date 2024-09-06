from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split the input string into a list of words
    words = numbers.split()
    # convert the list of words to a list of numbers
    numbers = [int(word) for word in words]
    # sort the list of numbers in ascending order
    numbers.sort()
    # join the numbers back into a string
    return ' '.join(str(i) for i in numbers)
