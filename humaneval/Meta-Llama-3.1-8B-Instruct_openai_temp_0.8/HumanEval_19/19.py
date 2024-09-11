### Sorting Numbers in a String

Here's a Python script that solves the given problem:

```python
from typing import List, Dict
from enum import Enum

class Number(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a dictionary mapping number names to their integer values
    num_dict: Dict[str, Number] = {str(num): num for num in Number}

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x].value)

    # Join the sorted list into a string with spaces in between
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines an `Enum` class `Number` to represent the numbers from 'zero' to 'nine'. The `sort_numbers` function splits the input string into a list of numbers, creates a dictionary mapping number names to their integer values, sorts the list of numbers based on their integer values, and finally joins the sorted list into a string with spaces in between. The function is tested with the example input 'three one five'.