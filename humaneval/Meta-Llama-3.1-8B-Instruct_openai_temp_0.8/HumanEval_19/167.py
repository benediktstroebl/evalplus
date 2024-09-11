```python
from typing import Dict, List

# Dictionary to map string numbers to integers
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    Args:
        numbers (str): A space-delimited string of numbers.
    
    Returns:
        str: A space-delimited string of numbers sorted from smallest to largest.
    """
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Convert the list to a list of integers using the dictionary
    num_list = [num_dict[num] for num in num_list]
    
    # Sort the list of integers
    num_list.sort()
    
    # Convert the list of integers back to a list of strings using the dictionary
    num_list = [list(num_dict.keys())[list(num_dict.values()).index(n)] for n in num_list]
    
    # Join the list of strings into a space-delimited string
    sorted_str: str =''.join(num_list)
    
    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, converts it to a list of integers, sorts the list, and then converts it back to a space-delimited string of numbers. The `num_dict` dictionary is used to map string numbers to integers.