```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a dictionary to map string numbers to their integer equivalents
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer equivalents
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five four'))  # Output: 'four five nine'
print(sort_numbers('zero seven six'))  # Output: 'zero six seven'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their integer equivalents, and returns the sorted string. It uses a dictionary to map string numbers to their integer equivalents and the built-in `sorted` function with a custom key function to perform the sorting. The example usage section demonstrates how to use the function with different input strings.