from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numbers_lst: List[int] = []
    for number in numbers.split():
        numbers_lst.append(int(number))
    numbers_lst.sort()

    return " ".join([str(number) for number in numbers_lst])

