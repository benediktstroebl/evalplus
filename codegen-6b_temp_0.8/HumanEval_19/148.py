from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # create a list of strings in the format 'zero', 'one', 'two' and assign numbers to them
    zero_one_two = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # if the first element is 'zero' ...
    if numbers[0] == 'zero':
        # return 'zero' followed by the numbers sorted
        return 'zero' + sort_numbers(numbers[1:])
        # ... otherwise ...
    else:
        # assign the numbers to the number list
        numbers = list(numbers)
        # sort the numbers
        numbers.sort()
        # return a string joining the numbers in the sorted order
        return ''.join(numbers)

