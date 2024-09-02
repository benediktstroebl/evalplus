from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Separate each number
    numbers_list = numbers.split()
    # Check to see if the list contains numbers that are not zero through nine
    check_nums(numbers_list)
    # Sort the list by value
    numbers_list.sort(key=int)
    # return the string with the numbers separated by a space
    return " ".join(numbers_list)

