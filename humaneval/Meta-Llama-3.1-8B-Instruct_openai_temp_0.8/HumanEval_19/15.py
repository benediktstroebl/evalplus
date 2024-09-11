### Python Function to Sort Numbers
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A string of space-delimited numbers.

    Returns:
        str: The sorted string of numbers.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary for mapping number strings to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()

    # Use a list comprehension to sort the numbers
    sorted_numbers: List[str] = sorted(numbers_list, key=lambda x: num_dict[x])

    # Join the sorted numbers back into a string separated by spaces
    sorted_string: str =''.join(sorted_numbers)

    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Outputs: 'one three five'
print(sort_numbers('nine four five'))  # Outputs: 'four five nine'
print(sort_numbers('eight seven seven'))  # Outputs:'seven seven eight'
```
This script defines a function `sort_numbers` that takes a string of space-delimited numbers as input, sorts them in ascending order, and returns the sorted string. It uses a dictionary to map each number string to its corresponding integer value, allowing it to sort the numbers correctly even when their string representations are different. The function then uses the `sorted` function with a custom sorting key to sort the numbers and joins the sorted list back into a string separated by spaces.