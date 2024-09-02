from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create empty list to store the sorted numbers
    sorted_numbers = []

    # Split the input string by space into a list of strings
    input_list = numbers.split()

    # Iterate over the input list and add each string to the sorted_numbers list
    for num in input_list:
        sorted_numbers.append(num)

    # Convert the sorted_numbers list to a string and return it
    return " ".join(sorted_numbers)
