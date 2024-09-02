from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split by space, build list from str
    number_list = numbers.split(" ")
    number_list = [int(num) for num in number_list]
    # sort numbers using built in sorted() function
    sorted_list = sorted(number_list)
    return ' '.join([str(num) for num in sorted_list])

