```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A string containing numberals separated by spaces.

    Returns:
        str: The input string with numberals sorted from smallest to largest.
    """

    # Define a dictionary to map numberals to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    num_list = numbers.split()

    # Sort the list of numberals based on their integer values
    sorted_list = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list back into a string separated by spaces
    sorted_str =''.join(sorted_list)

    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numberals as input, sorts them in ascending order, and returns the sorted string. The sorting is done by mapping each numeral to its integer value using a dictionary, then using Python's built-in `sorted` function with a custom sorting key.