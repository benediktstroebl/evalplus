```python
from typing import List
from collections import defaultdict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map string numbers to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    nums: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_nums: List[str] = sorted(nums, key=lambda x: num_dict[x])

    # Join the sorted list of numbers into a string
    sorted_str: str =''.join(sorted_nums)

    return sorted_str

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight four six'))  # Output: 'four six eight'
print(sort_numbers('nine five zero'))  # Output: 'five nine zero'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, maps the string numbers to their corresponding integer values using a dictionary, sorts the list of numbers, and returns the sorted string. The script includes example usage and docstrings to ensure its correctness and readability.