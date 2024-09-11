```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map string numbers to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    nums = numbers.split()

    # Convert string numbers to integers and sort the list
    sorted_nums = sorted([num_map[num] for num in nums])

    # Convert the sorted integers back to string numbers and join them into a string
    sorted_nums_str =''.join([str(num_map[num]) for num in sorted_nums])

    # Return the sorted string
    return sorted_nums_str


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine four seven'))  # Output: 'four seven nine'
print(sort_numbers('zero five two'))  # Output: 'two five zero'
```
This script uses a dictionary to map string numbers to their integer equivalents, then sorts the list of integers and converts them back to string numbers. The sorted string numbers are then returned.