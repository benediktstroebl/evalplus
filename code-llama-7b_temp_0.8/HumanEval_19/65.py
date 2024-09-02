from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # The list of numbers as integers.
    numbers_as_int: List[int] = [
        number_as_int(word) for word in numbers.split(' ') if word
    ]
    # Sort the numbers.
    numbers_as_int.sort()
    # Convert the numbers back to text.
    return ' '.join([
        number_as_word(number) for number in numbers_as_int
    ])

