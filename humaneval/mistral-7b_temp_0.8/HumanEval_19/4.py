from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # TODO: SOLUTION GOES HERE
    new_nums = []
    for num in numbers.split():
        new_nums.append(int(num))
    sorted_nums = sorted(new_nums)
    return ' '.join(str(num) for num in sorted_nums)

