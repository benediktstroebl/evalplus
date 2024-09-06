from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    sorted_numbers = []
    for num in numbers:
        try:
            num = int(num)
            sorted_numbers.append(num)
        except ValueError:
            pass
    sorted_numbers.sort()
    return ", ".join(sorted_numbers)

