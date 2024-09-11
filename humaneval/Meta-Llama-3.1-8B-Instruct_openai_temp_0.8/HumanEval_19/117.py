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
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a dictionary to map number names to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of numbers into a string
    sorted_str: str =''.join(sorted_list)

    return sorted_str


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine seven five'))  # Output: 'five seven nine'
print(sort_numbers('eight four one'))  # Output: 'one four eight'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers, sorts them based on their integer values, and returns the sorted string. The example usage demonstrates how to use the function with different input strings.