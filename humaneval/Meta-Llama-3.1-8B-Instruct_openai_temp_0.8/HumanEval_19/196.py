```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    Args:
        numbers (str): Space-delimited string of numbers
    
    Returns:
        str: The string with numbers sorted from smallest to largest
    """
    
    # Create a dictionary to map number names to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list based on the integer values of the numbers
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string separated by spaces
    sorted_numbers: str =''.join(sorted_num_list)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five')) # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers, sorts them based on their integer values, and returns the sorted string. The function uses a dictionary to map number names to their integer values, making it easy to add or remove number names without modifying the sorting logic. The example usage demonstrates how to call the function with a sample input string.