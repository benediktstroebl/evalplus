from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # ...
    # set the variable to 0 for sorting
    sort_list = []
    # split the string on spaces to get a list of strings
    # and convert the strings to integers
    for each_string in numbers.split():
        sort_list.append(int(each_string))
    # sort the list of integers in ascending order
    sort_list.sort()
    # convert the list of integers back to a string and return the string
    return ' '.join(map(str, sort_list))

