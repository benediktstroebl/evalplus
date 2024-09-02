from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    assert numbers.isalnum(), 'Input contains non-alphanumeric characters'

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

    list_of_numbers = numbers.split()
    try:
        sorted_list = sorted(list_of_numbers, key=lambda num: num_dict[num])
    except KeyError:
        raise ValueError('Input contains invalid numberals.')

    sorted_numbers = ' '.join(sorted_list)

    return sorted_numbers

