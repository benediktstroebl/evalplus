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
        numbers[i] = int(numbers[i])
    for i in range(len(numbers)):
        min_value = min(numbers)
        min_index = numbers.index(min_value)
        numbers[min_index] = numbers[i]
        numbers[i] = min_value
    return''.join([str(i) for i in numbers])

