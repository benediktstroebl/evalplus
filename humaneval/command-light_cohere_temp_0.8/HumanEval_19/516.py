```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are expected to be 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    # Sort numbers from smallest to largest
    numbers = [int(n) for n in numbers.
    numbers.sort()
    cause the matter with integers starting with zero and  nine,
        and only the valid numbers from the list above.
    return ' '.join(numbers)
    return

numbers = ['three one five', '7 two 8', 'four six', 'eight nine']
print(sort_numbers(numbers))
```