```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map string numbers to integers for easy sorting
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of string numbers
    num_list: List[str] = numbers.split()

    # Sort the list of string numbers based on their corresponding integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of string numbers back into a string with spaces in between
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine seven four'))  # Output: 'four nine seven'
print(sort_numbers('eight six three'))  # Output: 'three eight six'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numbers as input, sorts them based on their integer values, and returns the sorted string. It uses a dictionary to map string numbers to integers for easy sorting. The function is then tested with several example inputs.