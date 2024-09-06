```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    """
    return numbers.sort()
 stringsorted from smallest to largest. valid numbers in a numbers list, the numbers are sorted in ascending order.

test_sort_numbers = """
def test_sort_numbers():
    return sort_numbers("three one five")  # should return 'one three five'

# test suite begins here
"""

print(test_sort_numbers())
```