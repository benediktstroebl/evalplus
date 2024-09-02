from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # initialize empty list with valid numbers
    valid_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    sorted_numbers = []

    # split the input string into a list of numbers
    numbers = numbers.split()

    # loop through the numbers in the list
    for number in numbers:
        # check if the number is a valid number
        if number in valid_numbers:
            # add the number to the list of sorted numbers
            sorted_numbers.append(number)
        else:
            # if not, we have a non-valid number, we add it to a list of invalid numbers
            invalid_numbers.append(number)

    return ' '.join(sorted_numbers)
