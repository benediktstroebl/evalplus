from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # If the input string is empty, return an empty string
    if len(numbers) == 0:
        return ""

    # Remove all commas and then split the string into a list of numbers
    numbers = numbers.replace(",", "")
    numbers_list = numbers.split()

    # Sort the list of numbers
    numbers_list.sort()

    # Join the sorted list back into a string, separated by spaces
    return " ".join(numbers_list)

