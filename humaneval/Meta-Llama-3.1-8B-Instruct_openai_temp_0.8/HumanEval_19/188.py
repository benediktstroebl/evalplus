Here's a Python script to solve the problem:

```markdown
# Sort Numbers
=====================================

This script sorts a space-delimited string of numbers from 'zero' to 'nine'
in ascending order.

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted in ascending order.

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Map string representations of numbers to their numerical values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3,
        'four': 4, 'five': 5,'six': 6,'seven': 7,
        'eight': 8, 'nine': 9
    }

    # Split the string into a list of numbers
    num_list = numbers.split()

    # Sort the list of numbers based on their numerical values
    sorted_num_list = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list into a string
    sorted_string =''.join(sorted_num_list)

    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine seven eight'))  # Output:'seven eight nine'
print(sort_numbers('one one one'))  # Output: 'one one one'
```

This script uses a dictionary to map string representations of numbers to their numerical values. It then splits the input string into a list of numbers, sorts the list based on the numerical values, and joins the sorted list into a string. The sorted string is then returned as the result.