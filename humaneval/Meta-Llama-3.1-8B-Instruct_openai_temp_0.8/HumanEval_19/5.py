```python
from typing import Dict

# Mapping of string representations to integer values
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(sorted_list)

    return sorted_numbers

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script first maps the string representations of numbers to integer values using a dictionary. It then splits the input string into a list of numbers, sorts this list based on the integer values, and finally joins the sorted list back into a string. The result is the input string with numbers sorted from smallest to largest.