from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # create a set of numbers
    numbers_set = set()
    for number in numbers.split():
        numbers_set.add(int(number))

    # sort the numbers and return them as a string
    numbers_list = sorted(numbers_set)
    return ", ".join(str(num) for num in numbers_list)

