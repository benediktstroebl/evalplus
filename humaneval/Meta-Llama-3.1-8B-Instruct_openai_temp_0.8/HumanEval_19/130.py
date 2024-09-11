```python
from typing import List
from collections import OrderedDict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
    Args:
        numbers (str): A space-delimited string of numbers.
    
    Returns:
        str: The sorted string of numbers.
    """
    # Create a dictionary to map string numbers to integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    number_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(number_list, key=lambda x: number_map[x])
    
    # Use OrderedDict to remove duplicates while preserving order
    sorted_set: OrderedDict[str, None] = OrderedDict()
    for num in sorted_list:
        sorted_set[num] = None
    
    # Join the sorted list back into a string with spaces in between
    sorted_string: str =''.join(sorted_set.keys())
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
print(sort_numbers('seven three two four five one nine eight six'))  # Expected output: 'one seven three two four five six eight nine'
```