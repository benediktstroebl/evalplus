from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    new_numbers = []
    for number in numbers.split():
        number_value = int(number)
        if number_value < 0 or number_value > 9:
            raise ValueError("Invalid number in input")
        new_numbers.append(number_value)
    new_numbers = sorted(new_numbers)
    return " ".join([str(x) for x in new_numbers
