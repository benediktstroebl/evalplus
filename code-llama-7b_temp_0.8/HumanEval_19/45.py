from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    words = numbers.split()
    # Convert all words to numbers
    numbers = [get_number(word) for word in words]
    # Sort the numbers
    numbers.sort()
    # Join sorted numbers back into a string
    return ' '.join([str(number) for number in numbers])

