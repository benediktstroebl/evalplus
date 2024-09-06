Here's a self-contained Python script with a function that sorts numbers in Markdown format:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Returns the string with numbers sorted from smallest to largest.
    """
   
    sort_numbers('456 one 890 six three 907')
    'one eight seven six three nine'
```
This script defines a function sort_numbers that takes a string of numbers and sorts them in ascending order.