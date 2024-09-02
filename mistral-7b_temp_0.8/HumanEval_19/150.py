from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list: List[str] = numbers.split(" ")
    for i in range(0, len(numbers_list)):
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[i] > numbers_list[j]:
                numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]
    return " ".join(numbers_list)
