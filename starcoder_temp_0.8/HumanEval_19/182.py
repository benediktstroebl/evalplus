from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Input validation
    numbers_arr = numbers.split(" ")
    for num in numbers_arr:
        if num not in ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"):
            raise ValueError("Invalid number")

    # Code
    return " ".join(sorted(numbers_arr))

