from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    valid_choices = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    # convert string to list
    numbers_list: List[str] = numbers.split()

    # check if list contains valid choices,
    # and if not raise ValueError
    for number in numbers_list:
        if number not in valid_choices:
            raise ValueError('Not a valid choice')

    # convert list to int and sort the numbers
    numbers_list = sorted(map(int, numbers_list))

    # convert numbers back to string
    return ' '.join(map(str, numbers_list))

