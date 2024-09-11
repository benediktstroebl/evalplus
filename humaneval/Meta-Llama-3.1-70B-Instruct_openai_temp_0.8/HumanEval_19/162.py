```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words in ascending order.

    Args:
    numbers (str): A string containing space-delimited number words.

    Returns:
    str: The input string with number words sorted from smallest to largest.

    Raises:
    ValueError: If the input string contains invalid number words.
    """

    # Define a dictionary to map number words to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list = numbers.split()

    # Validate the input and convert number words to integers
    try:
        int_list = [num_dict[num] for num in num_list]
    except KeyError:
        raise ValueError("Invalid number word in input string")

    # Sort the list of integers and convert them back to number words
    sorted_num_list = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in sorted(int_list)]

    # Join the sorted number words back into a string
    sorted_numbers =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words, sorts them in ascending order, and returns the sorted string. It uses a dictionary to map number words to their corresponding integer values, validates the input, and handles errors. The test at the end demonstrates its usage.