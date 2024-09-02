from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a list of individual numbers in the string
    numbers_list: List[str] = numbers.split(" ")

    # Sort the list
    numbers_list.sort()

    # Join the list into a string
    sorted_numbers: str = " ".join(numbers_list)

    return sorted_numbers
