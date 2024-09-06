from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # TODO: Make your own list of all the numbers
    number_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # TODO: Turn the numbers from the input string into a list
    numbers_as_list = numbers.split()
    # TODO: Sort the numbers
    sorted_numbers = sorted(numbers_as_list)
    # TODO: Turn the sorted list into a string
    numbers_as_string = " ".join(sorted_numbers)
    return numbers_as_string

