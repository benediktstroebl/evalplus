from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    if numbers.count('zero') > 0:
        numbers = numbers.replace('zero', '0')
    if numbers.count('one') > 0:
        numbers = numbers.replace('one', '1')
    if numbers.count('two') > 0:
        numbers = numbers.replace('two', '2')
    if numbers.count('three') > 0:
        numbers = numbers.replace('three', '3')
    if numbers.count('four') > 0:
        numbers = numbers.replace('four', '4')
    if numbers.count('five') > 0:
        numbers = numbers.replace('five', '5')
    if numbers.count('six') > 0:
        numbers = numbers.replace('six', '6')
    if numbers.count('seven') > 0:
        numbers = numbers.replace('seven', '7')
    if numbers.count('eight') > 0:
        numbers = numbers.replace('eight', '8')
    if numbers.count('nine') > 0:
        numbers = numbers.replace('nine',
