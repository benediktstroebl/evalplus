```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The string with numbers sorted from smallest to largest.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Define a dictionary to map numbers to their integer values
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
print(sort_numbers('zero five one'))  # Output: 'one five zero'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their integer values, and returns the sorted string. The function uses a dictionary to map numbers to their integer values, allowing it to compare and sort the numbers correctly. The script also includes example use cases to demonstrate the function's behavior.