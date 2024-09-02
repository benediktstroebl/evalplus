from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split()
    sorted_numbers = []
    for number in numbers:
        if number.isdigit():
            sorted_numbers.append(int(number))
        else:
            return f"{number} is not a number"
    return sorted_numbers
