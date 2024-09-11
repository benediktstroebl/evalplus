```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Create a dictionary to map number words to their numerical values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their numerical values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string
    sorted_string: str =''.join(sorted_num_list)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script first creates a dictionary to map number words to their numerical values. It then splits the input string into a list of numbers, sorts this list based on the numerical values, and finally joins the sorted list back into a string. The script includes a test case to demonstrate its functionality.