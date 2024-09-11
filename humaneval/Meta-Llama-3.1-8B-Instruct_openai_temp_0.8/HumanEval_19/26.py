### Sorting Numbers in a String

Here's a Python function that sorts a string of numbers from smallest to largest.

```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of numbers from smallest to largest.

    Args:
    numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
    str: The string with numbers sorted from smallest to largest.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Define a dictionary to map string numbers to their integer values
    number_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: number_map[x])

    # Join the sorted list into a string with spaces in between
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
print(sort_numbers('five four three'))  # Output: 'three four five'
```

This function first defines a dictionary to map string numbers to their integer values. It then splits the input string into a list of numbers, sorts the list based on the integer values, and finally joins the sorted list into a string with spaces in between.