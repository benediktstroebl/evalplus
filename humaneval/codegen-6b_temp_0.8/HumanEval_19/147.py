from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Remove all spaces from the string
    numbers = numbers.replace(" ", "")
    # Split the string into a list of strings of numbers
    numbers = numbers.split(" ")

    # Empty string for sorted list of numbers
    sorted_numbers = ""

    # Loop through numbers in list
    for number in numbers:
        # If number not already in sorted list, add number to sorted list
        if number not in sorted_numbers:
            sorted_numbers += number + " "

    # Remove last space and return sorted list
    return sorted_numbers.strip()

