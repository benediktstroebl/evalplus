from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    lst_of_nums = []
    lst_of_chars = numbers.split()
    for char in lst_of_chars:
        lst_of_nums.append(char)
    lst_of_nums.sort()
    lst_of_nums = " ".join(lst_of_nums)
    return lst_of_nums

