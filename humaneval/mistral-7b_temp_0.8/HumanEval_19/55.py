from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    l = []
    for i in numbers.split():
        l.append(i)
    l.sort()
    res = ""
    for i in l:
        res += i
        res += " "
    res = res[:-1]
    return res

