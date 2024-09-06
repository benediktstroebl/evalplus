Here is a self-contained Python script with a function that solves the problem of sorting numbers in markdown code blocks:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Convert input to list of numbers
    numbers = [int(num) for num in numbers.
    # Sort the sort numbers from smallest to largest
    numbers.sort()
   ,
    # Convert sorted list back to string
    sorted_str = ' '.join(str(num) for num in numbers)
    return sorted_str
```