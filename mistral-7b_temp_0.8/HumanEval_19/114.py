from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_as_ints = []
    for number in numbers.split(" "):
        if number == 'zero':
            number_as_int = 0
        elif number == 'one':
            number_as_int = 1
        elif number == 'two':
            number_as_int = 2
        elif number == 'three':
            number_as_int = 3
        elif number == 'four':
            number_as_int = 4
        elif number == 'five':
            number_as_int = 5
        elif number == 'six':
            number_as_int = 6
        elif number == 'seven':
            number_as_int = 7
        elif number == 'eight':
            number_as_int = 8
        elif number == 'nine':
            number_as_int = 9
        else:
            raise ValueError("Invalid input")
        numbers_as_ints.append(number_as_int)
    numbers_as_ints.sort()
    return " ".join(map(str, numbers_as_
