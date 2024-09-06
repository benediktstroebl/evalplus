from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    nums_list: List[str] = numbers.split()
    nums_list = sorted(nums_list, key=lambda x: 'zero one two three four five six seven eight nine'.index(x))
    return ' '.join(nums_list)

