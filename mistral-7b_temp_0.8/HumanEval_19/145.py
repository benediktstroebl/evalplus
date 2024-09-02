from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_split = numbers.split(' ')
    numbers_list: List[int] = []
    for number in numbers_split:
        number_int = int(number)
        numbers_list.append(number_int)
    numbers_list.sort()
    numbers_sorted = ' '.join(str(number) for number in numbers_list)
    return numbers_sorted
