```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sort()

```
numbers = ['three one five', 'two six three']
test_sort_numbers = [
    "This will return numbers sorted from smallest to largest: 'one three five'",
    "Invalid input! Please choose from: zero, one, two, three, four, five, six, seven, eight, or nine."
]

# Function Test
def test_sort_numbers_func(t):
    return t == sort_numbers(t)

# Test cases
for test in test_sort_numbers:
    assert test_sort_numbers_func(test) == test == True
```