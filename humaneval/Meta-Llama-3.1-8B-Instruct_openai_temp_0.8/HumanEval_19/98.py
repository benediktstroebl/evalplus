### Number Sorter Script
#### Python Script to Sort Numbers from a Space-Delimited String
```python
from typing import List

# Dictionary mapping number names to their integer values
NUMBER_MAP = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number names (zero to nine) in ascending order.

    Args:
    numbers (str): Space-delimited string of number names.

    Returns:
    str: Sorted string of number names.
    """

    # Split input string into a list of number names
    number_list: List[str] = numbers.split()

    # Map number names to their integer values and sort
    sorted_list: List[str] = sorted(number_list, key=lambda x: NUMBER_MAP[x])

    # Join sorted list back into a string
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine four zero'))  # Output: 'zero four nine'
```
This script works by first splitting the input string into a list of number names. It then uses the `sorted` function to sort this list, using a lambda function to map each number name to its corresponding integer value. Finally, it joins the sorted list back into a string with spaces in between, and returns this string.