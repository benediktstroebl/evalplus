from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    sort_order = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                  'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers = numbers.split()
    for i in range(len(numbers)):
        numbers[i] = sort_order[numbers[i].lower()]
    numbers.sort()
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    return ' '.join(numbers)

