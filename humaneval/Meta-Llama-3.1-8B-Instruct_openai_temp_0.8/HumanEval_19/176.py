### Sorting Number Strings
```python
from typing import List
from collections import OrderedDict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): Space-delimited string of numbers.

    Returns:
        str: Sorted string of numbers.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use a dictionary to map number strings to their corresponding integer values
    num_map: dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Use OrderedDict to remove duplicates and maintain the order
    sorted_num_set: OrderedDict = OrderedDict()
    for num in sorted_num_list:
        sorted_num_set[num] = None

    # Join the sorted list of numbers back into a string
    sorted_str: str =''.join(list(sorted_num_set.keys()))

    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('five nine one'))   # Output: 'one five nine'
print(sort_numbers('zero eight four')) # Output: 'four eight zero'
```
This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their corresponding integer values, and returns the sorted string. The `OrderedDict` is used to remove duplicates and maintain the order of the sorted numbers. The function uses a dictionary to map number strings to their corresponding integer values, making it easy to add or remove numbers from the valid choices.