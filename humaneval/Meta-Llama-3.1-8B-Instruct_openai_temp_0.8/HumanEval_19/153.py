```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The sorted string of numbers
    """
    # Create a dictionary to map number words to their integer values
    number_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: number_dict[x])

    # Join the sorted list of numbers into a string
    sorted_string: str =''.join(sorted_num_list)

    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five three'))  # Output: 'three five nine'
print(sort_numbers('eight seven six'))  # Output:'six seven eight'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts the numbers from smallest to largest, and returns the sorted string. The function uses a dictionary to map number words to their integer values, and the built-in `sorted` function with a lambda function as the key to sort the list of numbers. The sorted list is then joined back into a string using the `join` method.