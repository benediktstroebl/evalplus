```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A string of space-delimited numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Convert the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Define a dictionary to map the string numbers to their integer equivalents
    num_map: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer equivalents
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine nine five'))  # Output: 'five nine nine'
print(sort_numbers('seven four one'))  # Output: 'one four seven'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them from smallest to largest, and returns the sorted string. The function uses a dictionary to map the string numbers to their integer equivalents, which are then used to sort the list of numbers. The sorted list is then joined into a string and returned. The script also includes some test cases to demonstrate the function's behavior.