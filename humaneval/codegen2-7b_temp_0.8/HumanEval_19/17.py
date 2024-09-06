from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.replace(' ', '')
    sort_number = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5','six': '6','seven': '7', 'eight': '8', 'nine': '9'}
    sorted_numbers = [sort_number[n] for n in numbers]
    return''.join(sorted_numbers)

