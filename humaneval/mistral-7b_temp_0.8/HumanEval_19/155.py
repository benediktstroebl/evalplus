from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_to_index = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers = numbers.split(' ')
    sorted_numbers = []
    for number in numbers:
        index = number_to_index[number]
        sorted_numbers.append(index)
    sorted_numbers = sorted(sorted_numbers)
    sorted_numbers_str = ''
    for num in sorted_numbers:
        sorted_numbers_str += str(num)
    return sorted_numbers_str

