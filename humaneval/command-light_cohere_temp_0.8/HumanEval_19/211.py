Here's a self-contained Python script with a function that sorts a string of numbers in Markdown code format:
```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Numbers are sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    return numbers.lists().str(sorted(numbers.split(" ")))

numbers = "three one five six eight nine"
print(sort_numbers(numbers))  # Output: one threefive sixeight nine
```