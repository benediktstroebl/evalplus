```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Create a dictionary to map the string representations to their integer values
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list of numbers back into a string separated by spaces
    sorted_string: str =''.join(sorted_num_list)
    
    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five four'))  # Output: 'four five nine'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their integer values, and returns the sorted string. The function uses a dictionary to map the string representations of numbers to their integer values, allowing the numbers to be sorted correctly.