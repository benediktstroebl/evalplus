from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # short circuit
    if numbers == 'zero':
        return 'zero'
    if numbers == 'nine':
        return 'nine'

    lst = numbers.split()
    lst = [int(num) for num in lst]
    lst.sort()
    lst = [str(num) for num in lst]
    return ' '.join(lst)

