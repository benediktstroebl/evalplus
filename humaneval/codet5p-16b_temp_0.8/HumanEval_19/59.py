from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    valid_choices = ['zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', 'nine']
    num_list = numbers.split()

    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])

    num_list.sort()
    return''.join([str(num) for num in num_list])

