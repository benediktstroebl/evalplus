from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = [x.lower() for x in numbers.split(" ")]
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
    numbers_list.sort()
    for i in range(len(numbers_list)):
        numbers_list[i] = str(numbers_list[i])
    return " ".join(numbers_list)

