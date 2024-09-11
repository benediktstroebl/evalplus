```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
    """

    # Create a dictionary to map number strings to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use a lambda function as the key for sorting
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_str =''.join(sorted_list)

    return sorted_str

# Example usage
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numbers as input, sorts them in ascending order, and returns the sorted string. It uses a dictionary to map number strings to their integer values, allowing for efficient comparison and sorting. The example usage demonstrates how to call the function and print the result.