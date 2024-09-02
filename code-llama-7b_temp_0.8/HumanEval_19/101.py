from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a dictionary with numberals as keys and indices as values
    number_to_indx = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # Create a list with numberals as values
    numbers_list = numbers.split()

    # Create a list with the values of the dictionary sorted
    numbers_list.sort(key=lambda num: number_to_indx[num])

    # Return a string of the list elements separated by spaces
    return " ".join(numbers_list)

