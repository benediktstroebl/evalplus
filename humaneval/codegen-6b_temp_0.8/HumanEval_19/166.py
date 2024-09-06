from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    ans = ''
    for char in numbers:
        if char == '0':
            ans += 'zero'
        elif char in ['1', '2', '3', '4']:
            ans += char
        elif char == '5':
            ans += 'five'
        elif char == '6':
            ans += 'six'
        elif char == '7':
            ans += 'seven'
        elif char == '8':
            ans += 'eight'
        elif char == '9':
            ans += 'nine'

    return ans

