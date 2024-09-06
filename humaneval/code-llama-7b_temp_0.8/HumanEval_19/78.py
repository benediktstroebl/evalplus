from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert str to list of strings, then convert each str to an int
    num_list = list(numbers.split(' '))
    num_list_int = list(map(int, num_list))

    # Use the sort method of the list class to sort the list in ascending order
    num_list_int.sort()

    # Convert list of ints to strings and join to a single string
    num_list_str = list(map(str, num_list_int))
    return ' '.join(num_list_str)

