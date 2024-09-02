from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Check if all numbers in the list are valid
    if len(numbers) == 0 or not all(num in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] for num in numbers.split()):
        raise ValueError("Input contains invalid numbers")

    numbers_list = [int(number) for number in numbers.split()]
    numbers_list.sort()
    return ' '.join([str(num) for num in numbers_list])

