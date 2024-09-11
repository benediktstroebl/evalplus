```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Sort a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numbers.

    Returns:
    str: The input string with numbers sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Define a dictionary to map number strings to their corresponding integers
    num_map: dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Use a lambda function as the key to sort the list based on the integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list into a string separated by spaces
    sorted_str: str =''.join(sorted_list)

    return sorted_str


# Example usage:
print(sort_numbers('three one five'))
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers, sorts them in ascending order based on their corresponding integer values, and returns the sorted string. The example usage at the end demonstrates how to use this function.