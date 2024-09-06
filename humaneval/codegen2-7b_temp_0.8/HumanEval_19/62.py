from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split(' ')
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if int(numbers[j]) > int(numbers[j + 1]):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return''.join(numbers
