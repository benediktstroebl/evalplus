from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    sort_array = ['zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', 'nine']
    sort_numbers_list = numbers.split()
    for i in range(len(sort_numbers_list)):
        sort_numbers_list[i] = sort_array.index(sort_numbers_list[i])
    sort_numbers_list.sort()
    sort_numbers_list = [str(i) for i in sort_numbers_list]
    return''.join(sort_numbers_list)

