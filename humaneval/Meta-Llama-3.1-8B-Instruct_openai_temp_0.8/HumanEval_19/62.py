```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The sorted string.
    """
    # Create a dictionary to map string numbers to integers
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list back into a string
    sorted_str: str =''.join(sorted_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('five seven eight six'))  # Output: 'five six seven eight'
print(sort_numbers('nine nine nine nine'))  # Output: 'nine nine nine nine'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numberals from 'zero' to 'nine', sorts them in ascending order, and returns the sorted string. The function uses a dictionary to map string numbers to integers for sorting purposes. It then splits the input string into a list of numbers, sorts the list based on their integer values, joins the sorted list back into a string, and returns the result. The script also includes test cases to demonstrate the function's correctness.