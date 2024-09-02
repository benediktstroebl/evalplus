from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split(' ')
    for i in range(len(numbers) - 1):
        for j in range(i, len(numbers)):
            if int(numbers[i]) > int(numbers[j]):
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return ' '.join(numbers)

