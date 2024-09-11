```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Convert the input string into a list of numbers and a dictionary for lookup
    num_list = numbers.split()
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the numbers based on their integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted numbers back into a string separated by spaces
    sorted_string =''.join(sorted_num_list)

    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers and returns the string with the numbers sorted from smallest to largest. The function uses a dictionary to map each number to its integer value, making it easy to compare and sort the numbers. The sorted numbers are then joined back into a string separated by spaces.