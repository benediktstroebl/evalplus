```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """

    # Create a dictionary to map string numbers to their integer equivalent
    number_mapping = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer equivalent
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: number_mapping[x])

    # Join the sorted list back into a string
    sorted_string: str =''.join(sorted_num_list)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine nine one'))   # Output: 'one nine nine'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them in ascending order based on their integer equivalent, and returns the sorted string. The function uses a dictionary to map string numbers to their integer equivalent, and the built-in `sorted` function with a lambda function as the key to sort the list of numbers. Finally, the script includes test cases to demonstrate the function's correctness.