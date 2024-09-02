from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = []
    numbers = numbers.replace(" ", "")
    for num in numbers:
        num_as_int = convert_num_to_int(num)
        numbers_list.append(num_as_int)
    numbers_list.sort()
    return " ".join(str(x) for x in numbers_list)

