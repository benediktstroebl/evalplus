```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Create a dictionary to map number strings to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string separated by spaces
    sorted_str: str =''.join(sorted_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine seven five'))  # Output: 'five seven nine'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, maps each number string to its integer value using a dictionary, sorts the list of numbers based on their integer values, and returns the sorted string. The script includes a docstring that provides documentation for the function, and includes test cases at the end to demonstrate its usage.