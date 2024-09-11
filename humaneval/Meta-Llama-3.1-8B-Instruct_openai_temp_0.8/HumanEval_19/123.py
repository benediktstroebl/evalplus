```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of numbers in the format 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers in ascending order.

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map numbers to their numerical values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use a lambda function with sorted to sort the list of numbers
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string separated by spaces
    sorted_str: str =''.join(sorted_num_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight four nine'))  # Output: 'four eight nine'
```

This script defines the `sort_numbers` function, which takes a string of space-delimited numbers as input, sorts them in ascending order based on their numerical values, and returns the sorted string. The function uses a dictionary to map number strings to their corresponding numerical values, allowing it to compare and sort the numbers correctly. The test cases at the end demonstrate the function's usage and output.