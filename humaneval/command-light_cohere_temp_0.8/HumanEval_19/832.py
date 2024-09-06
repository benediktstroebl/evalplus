```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(n) for n in numbers.
    if set(numbers) == {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}:
        return numbers[::-1].join(' ')
    else:
        return 'Invalid input'
numbers = 'three one five'
print(sort_numbers(numbers))  # Output: 'one three five'
```