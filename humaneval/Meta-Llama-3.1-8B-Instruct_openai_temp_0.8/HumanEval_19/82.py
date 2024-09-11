```python
from typing import Dict

# Define a dictionary to map number strings to their integer values
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The input string with numbers sorted from smallest to largest
    """

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Convert the list of numbers to a list of integers (using the num_dict)
    num_list_int: List[int] = [num_dict[num] for num in num_list]

    # Sort the list of integers in ascending order
    sorted_num_list_int: List[int] = sorted(num_list_int)

    # Convert the list of integers back to a list of strings (using the num_dict)
    sorted_num_list: List[str] = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in sorted_num_list_int]

    # Join the sorted list of strings into a single string with spaces in between
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Should print: "one three five"
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them from smallest to largest, and returns the sorted string. It uses a dictionary to map number strings to their integer values, allowing it to easily convert the input string to a list of integers, sort the list, and then convert it back to a string. The script includes a test case to verify the function's correctness.