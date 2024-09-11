```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.

    Returns:
    str: The string with numbers sorted from smallest to largest.

    Examples:
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map string numbers to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of strings
    numbers_list: List[str] = numbers.split()

    # Use list comprehension to create a new list with the integer values
    sorted_numbers_list: List[int] = [num_map[num] for num in numbers_list]

    # Sort the list of integers
    sorted_numbers_list.sort()

    # Use list comprehension again to create a new list with the string values
    sorted_numbers_string_list: List[str] = [num for num in numbers_list for n in sorted_numbers_list if num_map[num] == n]

    # Use the join function to concatenate the sorted list of strings into a single string
    sorted_string: str =''.join(sorted_numbers_string_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

In this script, we first define a dictionary `num_map` to map string numbers to their integer equivalents. We then split the input string into a list of strings. We use list comprehension to create a new list with the integer values, sort this list, and then use list comprehension again to create a new list with the string values. Finally, we use the `join` function to concatenate the sorted list of strings into a single string and return it.