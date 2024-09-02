from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split into list
    input_list = numbers.split(" ")
    # remove non-numbers
    input_list = [el for el in input_list if el in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]
    # convert to numbers
    input_list = [int(el[:-3]) for el in input_list]
    # sort
    input_list.sort()
    # convert to strings
    input_list = [str(el) for el in input_list]
    # join back into string
    return ' '.join(input_list)
