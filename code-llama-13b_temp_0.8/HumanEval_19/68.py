from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if not numbers:
        return ''

    # Initialise dictionary with keys being the string representation of number and values being the
    # number corresponding to each string.
    numberals = dict(zip(
        ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'),
        range(10)))

    num_list = []
    for num in numbers.split():
        if num in numberals:
            num_list.append(numberals[num])

    return ' '.join([k for k, v in sorted(numberals.items(), key=lambda item: item[1]) if v in num_list])

