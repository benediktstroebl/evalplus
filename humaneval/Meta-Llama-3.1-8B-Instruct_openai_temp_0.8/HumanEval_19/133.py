```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numbers from 'zero' to 'nine' 
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Create a dictionary to map string numbers to integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string separated by spaces
    sorted_str: str =''.join(sorted_list)
    
    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five four'))  # Output: 'four five nine'
print(sort_numbers('seven eight six'))  # Output:'six seven eight'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine', sorts them from smallest to largest, and returns the sorted string. The function uses a dictionary to map string numbers to integer values for sorting. It then splits the input string, sorts the list of numbers, and joins them back into a string before returning the result.