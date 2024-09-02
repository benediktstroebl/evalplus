from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Remove whitespace
    numbers = numbers.replace(" ", "")

    # Split the numbers based on each digit
    split_number = ["".join(x) for x in zip(*[iter(numbers)] * 3)]

    # Sort them based on the number that the element is
    final_numbers = [
        x + y
        for pair in zip(split_number[::2], split_number[1::2])
        for x, y in zip(*sorted(pair))
    ]

    # Rejoin them into a string
    return "".join(final_numbers)

