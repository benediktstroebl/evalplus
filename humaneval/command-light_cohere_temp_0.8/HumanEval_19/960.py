Certainly! Here's the Python script with the self-contained function and its test cases:
```python
import typing
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are strings are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sort()

```
numbers = "three one five"
test_string = sort_numbers(numbers)
print(test_string)  # Output: "one threefive"

numbers = "zero seven eight nine"
test_string = sort_numbers(numbers)
print(test_string)  # Output: "seven eight nine"

numbers = "five three six"
test_string = sort_numbers(numbers)
print(test_string)  # Output: "five three six"
```