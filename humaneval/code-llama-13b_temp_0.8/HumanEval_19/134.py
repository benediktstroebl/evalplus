from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Numbers in English
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # 1. Get the numbers from string
    numbers_list = numbers.split(' ')

    # 2. Get the numbers (as digits) from numbers_list
    number_digits = [number_dict[digit] for digit in numbers_list]

    # 3. Sort the number_digits
    number_digits.sort()

    # 4. Get the sorted numbers from number_digits
    sorted_numbers = [str(digit) for digit in number_digits]

    # 5. Return the sorted numbers as a space-separated string
    return ' '.join(sorted_numbers)

