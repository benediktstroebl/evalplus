from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # create mapping for the numbers
    mapping = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # split string into a list
    numbers = numbers.split(' ')

    # create new list of integers
    new_numbers: List[int] = []

    # iterate over numbers and use mapping to create int list
    for number in numbers:
        new_numbers.append(mapping[number])

    # sort numbers
    new_numbers.sort()

    # create sorted string
    sorted_string: str = ''
    for num in new_numbers:
        sorted_string += list(mapping.keys())[list(mapping.values()).index(num)] + ' '

    # remove trailing space
    sorted_string = sorted_string.strip()

    return sorted_string

