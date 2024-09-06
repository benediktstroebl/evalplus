```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers. 
    # Test: 
    input: "three one five"
    expected output: "one three five"
    """

numbers = "three one five"
sorted_nums = sort_numbers(numbers)
print(sorted_nums)  # Output: one threefive
```