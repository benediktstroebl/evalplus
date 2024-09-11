```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The sorted string of numbers.

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Define a dictionary to map string numbers to integer values
    num_map: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Convert the list of string numbers to a list of integer values
    int_list: List[int] = [num_map[num] for num in num_list]

    # Sort the list of integer values
    int_list.sort()

    # Convert the sorted list of integer values back to a list of string numbers
    sorted_list: List[str] = [list(num_map.keys())[list(num_map.values()).index(num)] for num in int_list]

    # Join the sorted list of string numbers into a string with spaces in between
    sorted_str: str =''.join(sorted_list)

    return sorted_str


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine four eight'))  # Output: 'four eight nine'
```

This script works by first splitting the input string into a list of numbers. Then it defines a dictionary to map string numbers to integer values. It converts the list of string numbers to a list of integer values using a list comprehension, sorts the list of integer values, and then converts the sorted list of integer values back to a list of string numbers. Finally, it joins the sorted list of string numbers into a string with spaces in between.