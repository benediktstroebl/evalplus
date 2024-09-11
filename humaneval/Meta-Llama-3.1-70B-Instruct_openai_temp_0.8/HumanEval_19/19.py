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

    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list = numbers.split()

    # Use the dictionary to sort the list of number words
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string and return it
    return''.join(sorted_list)


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words as input, sorts them in ascending order, and returns the sorted string. It uses a dictionary to map number words to their integer values, and the built-in `sorted` function to sort the list of number words. The sorted list is then joined back into a string and returned.