from typing import List
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from lowest to highest.
    
    Valid input includes 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    """
    numbers = input_string.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers