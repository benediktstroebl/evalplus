from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # split numbers into list
    number_list = numbers.split()
    # create mapping of numbers to ints
    num_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
               'nine': 9}
    # convert list of strings into list of ints
    num_list = [num_map[num] for num in number_list]
    num_list.sort()
    # convert list of ints back to list of strings
    num_list = [str(num) for num in num_list]
    # return string of sorted list
    return ' '.join(num_list)

