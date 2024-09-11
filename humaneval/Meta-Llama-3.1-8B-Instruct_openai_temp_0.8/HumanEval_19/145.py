### Sorting Numbers in a String

Here's a Python script that solves the problem:

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """

    # Define a dictionary to map number strings to their numerical values
    num_values = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their numerical values
    num_list.sort(key=lambda x: num_values[x])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them in ascending order, and returns the sorted string. The `num_values` dictionary maps each number string to its numerical value, which is used to sort the list of numbers. The sorted list is then joined back into a string using the `join` method. The script includes an example usage of the function at the end.