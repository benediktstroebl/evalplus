Certainly! Here is the improved Python script with a self-contained function `sort_numbers()` that solves the problem of sorting numbers in markdown format:

```python
import re
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return re.sub('(\\d+)', '', numbers)
    numbers = re.split(' ', numbers)
    sort(numbers)
    return numbers
```

This code uses the `re` module to split the input string into numbers, then applies the `sort` function to the list of numbers to sort them, and finally returns the list of numbers.