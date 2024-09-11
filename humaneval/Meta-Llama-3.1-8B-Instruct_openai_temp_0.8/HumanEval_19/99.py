```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the input string into a list of strings representing numbers
    numbers_list: List[str] = numbers.split()

    # Create a dictionary to store the numbers and their corresponding integer values
    num_dict: dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    sorted_numbers: List[str] = sorted(numbers_list, key=lambda x: num_dict[x])

    # Join the sorted list of numbers into a string
    sorted_numbers_str: str =''.join(sorted_numbers)

    return sorted_numbers_str

# Example usage:
print(sort_numbers('three one five'))
print(sort_numbers('nine eight seven'))
print(sort_numbers('zero four five'))
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their integer values, and returns the sorted string. The function uses a dictionary to map the string representations of numbers to their corresponding integer values for sorting purposes. The sorted list of numbers is then joined into a string with spaces in between. The example usage demonstrates the function's behavior with different input strings.