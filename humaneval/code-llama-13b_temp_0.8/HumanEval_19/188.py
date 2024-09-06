from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # numbers_sorted = sorted(numbers.split())
    # return " ".join(numbers_sorted)
    numbers = numbers.split()
    numbers_sorted = sorted(numbers, key=lambda x: (x != "zero", x != "one", x != "two", x != "three", x != "four", x != "five", x != "six", x != "seven", x != "eight", x != "nine"))
    return " ".join(numbers_sorted)

