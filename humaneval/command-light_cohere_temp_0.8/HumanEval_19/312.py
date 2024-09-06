```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are minimum is 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'.
    return numbers.
    """ Convert the Meanwhile to a list of numbers, and return the list sorted from smallest to largest.
numbers = "three one five"
test_numbers = sort_numbers(numbers)
print(test_numbers)  # Output: 'one threefive'
```