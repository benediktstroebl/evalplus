from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    nums = numbers.split()
    sorted_nums = []
    for num in nums:
        num_val = {'zero': 0,
                   'one': 1,
                   'two': 2,
                   'three': 3,
                   'four': 4,
                   'five': 5,
                   'six': 6,
                   'seven': 7,
                   'eight': 8,
                   'nine': 9}
        sorted_nums.append(str(num_val[num]))
    sorted_nums.sort()
    return ' '.join(sorted_nums)

