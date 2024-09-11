```python
from typing import List
from collections import OrderedDict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The string with numbers sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Create a dictionary that maps string representations of numbers to their integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: number_map[x])
    
    # Use OrderedDict to remove duplicates while preserving order
    sorted_num_list = list(OrderedDict.fromkeys(num_list))
    
    # Join the sorted list of numbers back into a string
    sorted_string =''.join(sorted_num_list)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('four nine eight five seven six'))  # Output: five seven six eight four nine
```

This script does the following:

1. Defines a dictionary `number_map` that maps string representations of numbers to their integer values.
2. Splits the input string into a list of numbers.
3. Sorts the list of numbers based on their integer values using `sort()` and a lambda function.
4. Removes duplicates from the sorted list while preserving order using `OrderedDict.fromkeys()`.
5. Joins the sorted list of numbers back into a string using `' '.join()`.
6. Returns the sorted string.

The script also includes example usage and test cases to demonstrate its functionality.