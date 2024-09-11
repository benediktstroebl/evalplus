```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Define a dictionary to map number names to their integer values
    num_values = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_values[x])

    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```

This script first defines a dictionary to map number names to their integer values. Then, it splits the input string into a list of numbers, sorts the list based on the integer values of the numbers, and finally joins the sorted list back into a string. The example usage at the end demonstrates how to use the `sort_numbers` function.