from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the string into a list of strings
    number_strings = numbers.split()  # type: List[str]
    # Create a list of numbers and sort it
    sorted_numbers = sorted([int(numeral) for numeral in number_strings])
    # Join the sorted numbers into a string
    return ' '.join(map(str, sorted_numbers))

