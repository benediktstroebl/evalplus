```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numerical words in ascending order.

    Args:
    numbers (str): A string of space-delimited numerical words (zero to nine).

    Returns:
    str: The input string with numerical words sorted in ascending order.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map numerical words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numerical words
    num_list = numbers.split()

    # Sort the list of numerical words based on their integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_string =''.join(sorted_num_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numerical words as input, sorts them in ascending order, and returns the sorted string. It uses a dictionary to map numerical words to their integer values and the built-in `sorted` function to sort the list of numerical words. The function is then tested with a few examples.