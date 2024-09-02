from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split()
    valid_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    if len(numbers_list) == 0:
        return ''

    for index, number in enumerate(numbers_list):
        if number not in valid_numbers:
            return ''
        numbers_list[index] = valid_numbers.index(number)

    numbers_list.sort()
    return ' '.join(str(number) for number in numbers_list)

