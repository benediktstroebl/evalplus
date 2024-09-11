### Number Sorter
#### A Python Script to Sort Numbers in a String

Here's a self-contained Python script that solves the problem:

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): Space-delimited string of numbers.

    Returns:
        str: Sorted string of numbers.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map number names to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: num_map[x])

    # Join the sorted list back into a string
    sorted_str: str =''.join(num_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five four'))  # Output: 'four five nine'
print(sort_numbers('zero eight seven'))  # Output: 'zero seven eight'
```

This script uses a dictionary to map number names to their integer values, allowing for efficient sorting based on these values. The `split()` method is used to split the input string into a list of numbers, which is then sorted using the `sort()` method. Finally, the sorted list is joined back into a string using the `join()` method.