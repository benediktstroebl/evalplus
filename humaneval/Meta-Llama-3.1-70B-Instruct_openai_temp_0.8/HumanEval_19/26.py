```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The string with numbers sorted from smallest to largest.
    """
    # Define a dictionary to map numberals to their corresponding integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    num_list = numbers.split()

    # Sort the list of numberals based on their corresponding integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list of numberals back into a string
    sorted_numbers =''.join(sorted_num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numberals as input, sorts the numberals based on their corresponding integer values, and returns the sorted string. The function uses a dictionary to map numberals to their corresponding integer values and the built-in `sorted` function to sort the list of numberals. The test case demonstrates the function's correctness.