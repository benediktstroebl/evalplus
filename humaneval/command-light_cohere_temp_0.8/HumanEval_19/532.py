```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are choice of numbers are: zero, one, two, three, four, five, six, seven, eight, and nine.
    numbers = [nums for the numbers in order from smallest to largest]
    return ' '.join(sorted(numbers))

numbers = ['three', 'one', 'five']
result = sort_numbers(numbers)
print(result)  # Output: one three five
```