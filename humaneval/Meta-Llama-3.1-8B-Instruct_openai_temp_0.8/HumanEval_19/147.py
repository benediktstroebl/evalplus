```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Sort numbers in a space-delimited string from smallest to largest.

    Args:
    numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
    str: The string with numbers sorted from smallest to largest.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map number words to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string with spaces in between
    sorted_str: str =''.join(sorted_num_list)

    return sorted_str

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script uses a dictionary to map number words to their integer values, splits the input string into a list of numbers, sorts the list based on the dictionary values, and joins the sorted list into a string with spaces in between.