```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.make_sequence(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
numbers = sort_numbers("three onefive")
print(numbers)
```