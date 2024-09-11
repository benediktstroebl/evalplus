```markdown
# Sorting Numbers in a String
=====================================

This script takes a space-delimited string of numbers as input, sorts them in ascending order, and returns the result as a string.

### Code
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Define a dictionary to map number strings to their integer values
    num_dict: dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of numbers into a string
    sorted_string: str =''.join(sorted_num_list)

    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Outputs: 'one three five'
print(sort_numbers('nine eight seven'))  # Outputs:'seven eight nine'
```

### Explanation

1. The `sort_numbers` function takes a space-delimited string of numbers as input.
2. It splits the input string into a list of numbers using the `split` method.
3. A dictionary `num_dict` is defined to map number strings to their integer values.
4. The list of numbers is sorted based on their integer values using the `sorted` function with a lambda function as the `key` argument.
5. The sorted list of numbers is joined into a string using the `join` method.
6. The sorted string is returned as the result.