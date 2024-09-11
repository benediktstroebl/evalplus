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
        str: The input string with numbers sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map number strings to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Use the dictionary to convert the list to a list of integers
    num_list = [num_dict[num] for num in num_list]

    # Sort the list of integers
    num_list.sort()

    # Convert the list of integers back to a list of number strings
    num_list = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_list]

    # Join the list of number strings back into a string
    sorted_string =''.join(num_list)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
print(sort_numbers('five five five'))  # Output: 'five five five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them in ascending order, and returns the sorted string. The function uses a dictionary to map number strings to their integer values, allowing it to easily convert the input string to a list of integers, sort them, and then convert them back to a list of number strings. Finally, it joins the list of number strings back into a string and returns the result.