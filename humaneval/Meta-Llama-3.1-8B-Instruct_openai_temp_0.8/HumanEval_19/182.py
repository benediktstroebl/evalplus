### Sorting Numbers in a String

Below is a Python script that sorts numbers in a string based on the provided problem statement.

```python
from typing import Dict


def sort_numbers(numbers: str) -> str:
    """
    Sorts numbers in a string from smallest to largest.
    
    Args:
    numbers (str): A space-delimited string of numbers.
    
    Returns:
    str: The string with numbers sorted from smallest to largest.
    
    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Define a dictionary to map number names to their corresponding integer values
    number_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: number_map[x])
    
    # Join the sorted list into a string with spaces in between
    sorted_numbers: str =''.join(num_list)
    
    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five zero'))  # Output: 'zero five nine'
```

This script defines a function `sort_numbers` that takes a string of numbers as input, sorts them based on their integer values, and returns the sorted string. The sorting is done using a dictionary to map each number name to its corresponding integer value, allowing for easy comparison and sorting. The script also includes example usage to demonstrate the function's behavior.