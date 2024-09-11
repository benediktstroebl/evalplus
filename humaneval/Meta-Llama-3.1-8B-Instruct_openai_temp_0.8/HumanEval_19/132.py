```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Define a dictionary to map string numbers to their integer equivalents
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer equivalents
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])
    
    # Join the sorted list back into a string
    sorted_numbers: str =''.join(sorted_num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five seven'))  # Output: 'five seven nine'
```

This script defines the `sort_numbers` function that takes a space-delimited string of numbers as input, sorts them based on their integer equivalents, and returns the sorted string. It uses a dictionary to map string numbers to their integer equivalents, and the `sorted` function with a custom key function to perform the sorting. The function is then tested with sample inputs to demonstrate its correctness.