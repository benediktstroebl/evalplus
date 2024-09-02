from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # splitting the string and converting it to list
    numbers_list: List[str] = numbers.split()
    # sorting the list
    numbers_list.sort()
    # returning the string
    return ' '.join(numbers_list)

