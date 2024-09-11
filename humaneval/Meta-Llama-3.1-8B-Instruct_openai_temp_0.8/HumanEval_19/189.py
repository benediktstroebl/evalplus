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
        str: The string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map string numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_str =''.join(sorted_num_list)

    return sorted_str


# Test the function
print(sort_numbers('three one five'))  # Outputs: 'one three five'
print(sort_numbers('nine eight seven'))  # Outputs:'seven eight nine'
print(sort_numbers('five four three two one zero'))  # Outputs: 'zero one two three four five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their integer values, and returns the sorted string. It uses a dictionary to map the string numbers to their integer values, and the `sorted` function with a lambda function as the key to sort the list of numbers. The sorted list is then joined back into a string using the `join` method. The function is tested with several example inputs to demonstrate its correctness.