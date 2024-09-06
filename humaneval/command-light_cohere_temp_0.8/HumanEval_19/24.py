```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ')
    how all numbers are sorted
    <numbers>
    <numbers> = sorted(numbers)
    return ' '.join(numbers)

numbers = ['three one five', 'two six seven eight nine']
print(sort_numbers(numbers))  # Output: one two three four five six seven eight nine
```