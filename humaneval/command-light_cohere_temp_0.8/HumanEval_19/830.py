```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return sorted(numbers.split())
sort(numbers)
#  tests:
numbers = "three one five"
assertEqual(sort_numbers(numbers), "one three five")
numbers = "two six three"
assertEqual(sort_numbers(numbers), ["two"," six"," three"])
numbers = "abc123 456"
assertEqual(sort_numbers(numbers), "abc123 456")
```