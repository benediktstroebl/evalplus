from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # TODO: ERROR HANDLING AND EXCEPTIONS
    # TODO: TESTS
    # TODO: DOCSTRING

    valid_nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                  5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    nums = list(map(lambda s: valid_nums[int(s)], numbers.split(' ')))
    nums.sort()
    return ' '.join(nums)
