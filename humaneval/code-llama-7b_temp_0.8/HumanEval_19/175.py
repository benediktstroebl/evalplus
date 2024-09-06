from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    nums = numbers.split()
    num_len = len(nums)
    for i in range(num_len):
        for j in range(num_len - 1):
            if len(nums[j]) == len(nums[j + 1]):
                if ord(nums[j][-1]) > ord(nums[j + 1][-1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return ' '.join(nums)

