from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input into a list of strings
    numbers_list = numbers.split()
    
    # Sort the list of strings in ascending order
    numbers_list.sort()
    
    # Convert the sorted list of strings back to a string
    numbers_string = ' '.join(numbers_list)
    
    return numbers_string

