from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Replace the strings with values
    values = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    # Convert input string to list of strings
    numbers_list = numbers.split()
    # Convert list of strings to list of values
    numbers_list = [values[item] for item in numbers_list]
    # Sort numbers_list
    numbers_list.sort()
    # Convert list of values back to list of strings
    numbers_list = [str(item) for item in numbers_list]
    # Convert list of strings to string
    numbers_list = " ".join(numbers_list)
    # Return string
    return numbers_list

