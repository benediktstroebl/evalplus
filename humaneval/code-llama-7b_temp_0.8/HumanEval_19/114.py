from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # valid choices from problem
    choices = {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}

    # convert str to a list of numberals
    num_list: List = numbers.split(' ')
    # remove any elements that are not in choices
    num_list = [x for x in num_list if x in choices]

    # sort list in place
    num_list.sort()

    # convert list back to str
    return ' '.join(num_list)

