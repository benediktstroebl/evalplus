```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """

    # Define a dictionary to map string numbers to their integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list = sorted(num_list, key=lambda x: number_map[x])

    # Join the sorted list into a string separated by spaces
    sorted_string =''.join(sorted_num_list)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five four'))  # Output: 'four five nine'
```

This Python script solves the problem by defining a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their integer values, and returns the sorted string. The function uses a dictionary to map string numbers to their integer values, which allows it to sort the numbers correctly. The test cases demonstrate the function's correctness.