```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map number words to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string and return the result
    return''.join(sorted_list)


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script works by first creating a dictionary to map number words to their integer values. It then splits the input string into a list of number words, sorts this list based on the integer values of the number words, and finally joins the sorted list back into a string. The `sorted` function's `key` argument is used with a `lambda` function to specify that the sorting should be based on the integer values of the number words.