from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Get all the numbers
    numbers = numbers.split(" ")

    # Number pairs
    number_pairs = {}

    # Sort by key
    for number in numbers:
        number_pairs[number] = len(number)

    # Return sorted numbers
    return " ".join([key for key, value in sorted(number_pairs.items(), key=lambda item: item[1])])
