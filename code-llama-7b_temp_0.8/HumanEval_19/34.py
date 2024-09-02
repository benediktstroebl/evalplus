from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    number_list = numbers.split()

    # Check for invalid entries
    for number in number_list:
        if number not in ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
            raise ValueError(f'Invalid input: {number}.')

    # Sort number_list
    number_list.sort(key=lambda x: (x != 'zero', x), reverse=True)

    return ' '.join(number_list)

