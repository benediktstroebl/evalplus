**Sorting Numbers from a String**
=====================================

Below is the Python script that solves the problem:

```python
from typing import Dict
from functools import cmp_to_key

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine'.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The string with numbers sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map string numbers to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers using a custom comparison function
    num_list.sort(key=lambda x: num_dict[x], reverse=False)

    # Join the sorted list back into a string
    sorted_str: str =''.join(num_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script uses a dictionary to map string numbers to their integer values, allowing for efficient comparison of the numbers. The `sort` method is used to sort the list of numbers, and the `join` method is used to combine the sorted list back into a string.