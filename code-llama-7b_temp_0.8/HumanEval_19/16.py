from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numberals: List[str] = numbers.split(" ")
    sorted_nums: List[str] = sorted(numberals, key=lambda x: [int(num) for num in x])

    return " ".join(sorted_nums)

