from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # First, convert a string to a list of numbers
    # and a list of strings
    num_strings, nums = [], []
    for num in numbers.split():
        if num == 'zero':
            nums.append(0)
            num_strings.append('zero')
        elif num == 'one':
            nums.append(1)
            num_strings.append('one')
        elif num == 'two':
            nums.append(2)
            num_strings.append('two')
        elif num == 'three':
            nums.append(3)
            num_strings.append('three')
        elif num == 'four':
            nums.append(4)
            num_strings.append('four')
        elif num == 'five':
            nums.append(5)
            num_strings.append('five')
        elif num == 'six':
            nums.append(6)
            num_strings.append('six')
        elif num == 'seven':
            nums.append(7)
            num_strings.append('seven')
        elif num == 'eight':
            nums.append(8)
            num_strings.append('eight')
        elif num == 'nine':
            nums.append(9)
            num_strings.append('nine')
    # We want to sort these lists so we can
    # merge them back together in the desired order
    num_strings.sort()
    nums.sort()
    return ' '.join([*map(str, nums), *num_strings])

