from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # TODO: Check for valid input
    # TODO: Check if len(numbers) == 0
    # TODO: Check if numbers only contains valid input

    # 1. Create a dict of number to index
    num_to_index = {
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

    # 2. Create a list of numbers with original order
    numbers_list = numbers.split(' ')

    # 3. Create a list of indices
    indices = [num_to_index[n] for n in numbers_list]

    # 4. Sort the indices
    indices.sort()

    # 5. Create a list of numbers in correct order
    nums_sorted = [numbers_list[i] for i in indices]

    # 6. Return string of numbers in correct order
    return ' '.join(nums_sorted)

