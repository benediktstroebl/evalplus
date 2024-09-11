### Sorting Numbers in a String

Here's a Python script that solves the problem:

```python
from typing import Dict

# Define a dictionary to map string numbers to their integer equivalents
number_map: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numbers.

    Returns:
    str: The input string with numbers sorted in ascending order.
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer equivalents
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: number_map[x])

    # Join the sorted list of numbers into a string
    sorted_string: str =''.join(sorted_num_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one'))  # Output: 'one two three four five six seven eight nine'
```

This script defines a dictionary `number_map` to map string numbers to their integer equivalents. The `sort_numbers` function splits the input string into a list of numbers, sorts the list based on the integer equivalents of the numbers, and then joins the sorted list into a string. The script includes example use cases to demonstrate the function's behavior.