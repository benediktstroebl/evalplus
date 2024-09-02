from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    def sort_num(nums: List[str]):
        numbers = [i for i in nums if i != '']
        return sorted(numbers)

    numbers = numbers.split()
    # numbers.remove('')
    return ' '.join(sort_num(numbers))
