```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are numbers are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(x) for x in numbers.
    numbers.sort()
    Furthermore namesorted string
    numbers in descending order.
    return ' '.join(numbers)

numbers = "three one five"
print(sort_numbers(numbers))
```