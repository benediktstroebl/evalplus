from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    num_dict = {
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

    # Convert the string of numberals to a list of integers
    num_list = [num_dict[num] for num in numbers.split()]

    # Sort the list of integers
    sorted_list = sorted(num_list)

    # Convert the list of integers back to a string of numberals
    sorted_numbers = ' '.join([list(num_dict.keys())[list(num_dict.values()).index(num)] for num in sorted_list])

    return sorted_numbers
