### Sorting Numbers in a String
#### Problem Description
The problem requires a Python function `sort_numbers` that takes a space-delimited string of numbers (from 'zero' to 'nine') as input, sorts them in ascending order, and returns the sorted string.

#### Solution
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The sorted string of numbers.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map number names to their integer values
    number_values = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    number_list: List[str] = numbers.split()

    # Map each number to its integer value and sort the list
    sorted_list: List[str] = sorted(number_list, key=lambda x: number_values[x])

    # Join the sorted list into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them in ascending order based on their integer values, and returns the sorted string. The `number_values` dictionary is used to map number names to their integer values, allowing the function to perform the sorting correctly. The `sorted` function with a lambda function as the key is used to sort the list of numbers. Finally, the sorted list is joined into a string separated by spaces, which is the output of the function.