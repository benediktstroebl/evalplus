```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numbers

    Returns:
    str: The sorted string with numbers
    """
    
    # Define a dictionary to map string numbers to integers
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Replace string numbers with their integer equivalents in the list
    num_list = [num_dict[num] for num in num_list]
    
    # Sort the list of numbers
    num_list.sort()
    
    # Replace the integer numbers with their string equivalents
    num_list = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_list]
    
    # Join the sorted list of numbers with spaces
    sorted_numbers =''.join(num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them from smallest to largest, and returns the sorted string. It first splits the input string into a list of numbers, replaces string numbers with their integer equivalents, sorts the list of numbers, and then replaces the integer numbers with their string equivalents before joining them back into a string.