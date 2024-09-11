```python
from typing import Dict


def sort_numbers(numbers: str) -> str:
    """ 
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Mapping of numbers to their corresponding integer values
    num_to_int: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_to_int[x])

    # Join the sorted list of numbers into a string
    sorted_str: str =''.join(sorted_list)

    return sorted_str


# Example usage:
print(sort_numbers('three one five'))  # Output: one three five
```

This script uses a dictionary to map the string representations of numbers to their corresponding integer values. It then splits the input string into a list of numbers, sorts this list based on the integer values, and finally joins the sorted list back into a string. The result is the input string with its numbers sorted from smallest to largest.