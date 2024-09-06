from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split()

    # Convert each number into an integer, then use a sort to place numbers in ascending order
    sorted_numbers = sorted(int(num) for num in numbers)

    # Convert numbers back into a string
    sorted_string = ' '.join(map(str, sorted_numbers))

    return sorted_string

