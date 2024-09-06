from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in numbers.split():
        try:
            numbers_list[int(number)] = numbers_list[int(number)]
        except IndexError:
            return "Invalid choice"
    return ' '.join([str(n) for n in numbers_list])

