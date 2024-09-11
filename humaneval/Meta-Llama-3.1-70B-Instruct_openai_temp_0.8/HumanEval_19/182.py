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
    # Create a dictionary that maps word numbers to their integer equivalent
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of word numbers
    word_nums = numbers.split()

    # Sort the list based on the integer equivalent of each word number
    sorted_word_nums = sorted(word_nums, key=lambda x: num_map[x])

    # Join the sorted list back into a string
    return''.join(sorted_word_nums)


# Example usage:
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

This script works by first defining a mapping between word numbers and their integer equivalents. It then splits the input string into a list of word numbers, sorts this list based on the integer equivalents, and finally joins the sorted list back into a string. The result is a string with the word numbers sorted from smallest to largest.