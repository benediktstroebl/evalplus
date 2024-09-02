from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    #list of numbers in string
    list_of_numbers = numbers.split(' ')

    #create list for numbers in the correct order
    numbers_in_order = ['zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', 'nine']

    #sort numbers in list
    sorted_numbers = sorted(list_of_numbers, key=lambda x: numbers_in_order.index(x))

    #create string from numbers in order
    sorted_numbers_str = " ".join(sorted_numbers)

    return sorted_numbers_str
