```python
from typing import Dict

# Create a dictionary to map string numbers to their integer equivalents
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

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
    
    # Use the sorted function with a custom key function to sort the list
    # The key function uses the num_dict dictionary to map string numbers to integers
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string with spaces in between
    sorted_str: str =''.join(sorted_list)
    
    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
print(sort_numbers('zero five one'))  # Output: 'one five zero'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numbers, sorts them from smallest to largest, and returns the sorted string. The function uses a dictionary to map string numbers to their integer equivalents, and the built-in `sorted` function with a custom key function to sort the list. The script includes test cases at the end to demonstrate the function's behavior.