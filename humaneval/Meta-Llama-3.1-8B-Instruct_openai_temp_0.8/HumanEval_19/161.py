```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    This function sorts numbers in a given string from smallest to largest.
    
    Parameters:
    numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.
    
    Returns:
    str: The string with numbers sorted from smallest to largest.
    """
    
    # Define a dictionary to map number strings to their corresponding integers
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: list[str] = numbers.split()
    
    # Sort the list of numbers based on their corresponding integer values
    num_list.sort(key=lambda x: num_dict[x])
    
    # Join the sorted list of numbers back into a string
    sorted_string: str =''.join(num_list)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script uses a dictionary to map number strings to their corresponding integers, then sorts the list of numbers based on these integer values. The sorted list is then joined back into a string, which is returned as the result. The function includes a docstring that explains its purpose, parameters, and return value, as well as example usage and a test case.