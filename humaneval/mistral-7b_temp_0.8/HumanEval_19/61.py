from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Your code here
    numbers_as_list = numbers.split()
    numbers_as_list.sort()
    sorted_numbers_as_list = [str(number) for number in numbers_as_list]
    return ' '.join(sorted_numbers_as_list)

