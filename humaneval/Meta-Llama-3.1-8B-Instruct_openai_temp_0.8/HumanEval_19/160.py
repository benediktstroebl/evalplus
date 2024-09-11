### Number Sorting Script

This script sorts a string of space-delimited numbers from 'zero' to 'nine' in ascending order.

```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Define a dictionary to map number strings to their integer values
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list back into a string
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numbers as input, sorts them in ascending order, and returns the sorted string. The `num_map` dictionary is used to map number strings to their integer values, allowing the function to compare and sort the numbers correctly.