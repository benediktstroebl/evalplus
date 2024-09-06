Here's a self-contained Python function that solves the problem you described:
```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split().
   numbers = list(numbers.map(c for c in '23456789'))
    return ''.join(numbers)
```
The function splits the input into a list of digits, then maps each digit to its corresponding number (0-based) and finally joins the numbers back together into a string.

This is a self-contained solution to the problem of sorting numbers in markdown code blocks.