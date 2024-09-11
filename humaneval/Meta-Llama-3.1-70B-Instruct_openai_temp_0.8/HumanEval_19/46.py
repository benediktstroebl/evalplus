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
    # Define a dictionary to map word numbers to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of word numbers
    num_list = numbers.split()

    # Sort the list of word numbers based on their integer equivalents
    sorted_list = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list of word numbers into a string and return
    return''.join(sorted_list)


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This Python script first defines a dictionary to map word numbers to their integer equivalents. It then splits the input string into a list of word numbers, sorts the list based on the integer equivalents, and finally joins the sorted list into a string for output.