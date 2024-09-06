from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # 1. Split into a list
    numbers = numbers.split(' ')

    # 2. Convert each list item to a number
    numbers = [int(number) for number in numbers]

    # 3. Sort the numbers
    numbers.sort()

    # 4. Convert each number to a numberal
    numbers = [str(number) for number in numbers]

    # 5. Join the numberal list into a string
    numbers = ' '.join(numbers)

    return numbers

