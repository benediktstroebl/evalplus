from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    result = [str(i) for i in range(10)]
    num_list = numbers.split(' ')
    num_list = [i for i in num_list if i in result]
    num_list.sort(key=lambda x: int(x))
    return''.join(num_list)

