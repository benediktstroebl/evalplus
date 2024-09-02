from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    sorted_list = []
    for i in numbers.split():
        if int(i) < 10:
            sorted_list += [i]
        else:
            sorted_list += [i[0] + str(int(i[1]) % 10)]
    return ' '.join(sorted_list)

