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
    # Create a dictionary to map the word representation of numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of words
    num_list = numbers.split()

    # Sort the list of words based on their integer values
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string separated by spaces
    sorted_str =''.join(sorted_list)

    return sorted_str


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numberals as input, sorts them based on their integer values, and returns the sorted string. The sorting is done using a dictionary to map the word representation of numbers to their integer values. The `sorted` function is used with a lambda function as the `key` argument to sort the list of words based on their integer values.