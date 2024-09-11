```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'

    :param numbers: A space-delimited string of numberals
    :return: The sorted string
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Dictionary to map number strings to their integer equivalents
    num_map: dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer equivalents
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list into a string separated by spaces
    sorted_str: str =''.join(sorted_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
print(sort_numbers('five nine seven'))  # Expected output: 'five seven nine'
print(sort_numbers('zero eight one'))  # Expected output: 'zero one eight'
```

This Python script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts the numbers from smallest to largest, and returns the sorted string. The function uses a dictionary to map the number strings to their integer equivalents, allowing it to compare and sort the numbers correctly. The script also includes test cases to demonstrate the function's correctness.