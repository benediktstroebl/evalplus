from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Step 1: convert the string to a list of integers
    numbers_list = [int(num) for num in numbers.split()]

    # Step 2: sort the list in ascending order
    numbers_list.sort()

    # Step 3: convert the list back to a string, with each number separated by a space
    return " ".join(str(num) for num in numbers_list)

