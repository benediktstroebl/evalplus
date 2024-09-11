### Sorting Numbers in a String
#### Problem Statement
Given a space-delimited string of numbers from 'zero' to 'nine', sort the numbers in ascending order.

#### Solution
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The sorted string of numbers.

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list of numbers back into a string
    sorted_string =''.join(num_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```
This script first defines a dictionary to map number words to their integer values. It then splits the input string into a list of numbers, sorts the list based on the integer values, and finally joins the sorted list back into a string. The function returns the sorted string.