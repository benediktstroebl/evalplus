from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    alphas = {'zero': '0', 'one': '1', 'two': '2', 'three': '3',
              'four': '4', 'five': '5', 'six': '6', 'seven': '7',
              'eight': '8', 'nine': '9'}
    previous_chars = []
    for n in numbers:
        if n not in alphas:
            return '{} is not a number'.format(n)
        else:
            if n == previous_chars[-1]:
                return 'Number {} is not sorted'.format(n)
            previous_chars.append(n)
            previous_chars.sort()
    return ''.join(previous_chars)

