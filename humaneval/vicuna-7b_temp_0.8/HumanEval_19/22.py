from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map each number to its position in the number line
    # The key is the string representation of the number (e.g. 'three' for 3)
    # The value is the position of the number in the number line (e.g. 3 for the 3rd number)
    number_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    # Create a list of numbers as strings
    numbers_str = [number_map[number] for number in numbers.split()]
    # Sort the list of numbers in ascending order
    numbers_str = sorted(numbers_str)
    # Join the sorted list of numbers into a single string
    return ' '.join(numbers_str)

