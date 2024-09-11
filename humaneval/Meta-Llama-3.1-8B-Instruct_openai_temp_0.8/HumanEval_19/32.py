### Sort Numbers from String
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The sorted string of numbers.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map the numbers to their integer values
    num_values = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9}

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_values[x])

    # Join the sorted list of numbers back into a string
    sorted_string: str =''.join(sorted_num_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```