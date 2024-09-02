from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    num_list = [int(s) for s in numbers.split()]
    sorted_num_list = sorted(num_list)
    sorted_num_str = " ".join(str(n) for n in sorted_num_list)
    return sorted_num_str

