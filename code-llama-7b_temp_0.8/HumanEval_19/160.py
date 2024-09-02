from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Note: This solution is not particularly efficient or elegant.
    # It works on the assumption that all inputs contain valid numbers and that all numbers are unique.

    # We assume that all input numbers are unique (not tested for).
    # We don't need to convert them to numbers, as the sort will work just fine.
    numbers = numbers.split()

    # Convert numberals to numbers
    converted_numbers = []
    for number in numbers:
        converted_numbers.append(number_to_numberal(number))

    # Perform the sort
    sorted_numbers = sorted(converted_numbers)

    # Convert numbers back to numberals
    converted_sorted_numbers = []
    for number in sorted_numbers:
        converted_sorted_numbers.append(numberal_to_number(number))

    return ' '.join(converted_sorted_numbers)

