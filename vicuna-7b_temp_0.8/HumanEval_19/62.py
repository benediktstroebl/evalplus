from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a list of numbers
    numbers_list = numbers.split()

    # Shuffle the list
    random.shuffle(numbers_list)

    # Convert the list to a string and return it
    numbers_string = ' '.join(numbers_list)
    return numbers_string
