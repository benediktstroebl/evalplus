```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The input string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Define a dictionary to map string numbers to their integer values
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string separated by spaces
    sorted_str: str =''.join(sorted_list)

    return sorted_str


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers and returns the sorted string. It uses a dictionary to map string numbers to their integer values, then sorts the list of numbers based on these values. The sorted list is then joined into a string and returned. The script also includes a test case to demonstrate the function's usage.