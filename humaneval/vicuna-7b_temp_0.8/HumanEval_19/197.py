from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # First, split the input string into a list of numbers
    numbers_list = [int(number) for number in numbers.split()]

    # Sort the list in ascending order
    numbers_list.sort()

    # Convert the sorted list back to a string
    sorted_numbers_list = [str(number) for number in numbers_list]

    # Concatenate the sorted numbers back into a string
    return ' '.join(sorted_numbers_list)
