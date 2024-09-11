```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A string containing space-delimited numbers from 'zero' to 'nine'.

    Returns:
    str: The input string with numbers sorted from smallest to largest.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Define a dictionary to map number words to their integer equivalents
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list = numbers.split()
    
    # Sort the list of number words based on their integer equivalents
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string
    sorted_string =''.join(sorted_list)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```