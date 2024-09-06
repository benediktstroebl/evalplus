```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list."""
    return [x + y if y != 0 else x + delimeter + str(y) for x, y in zip(numbers, numbers[1:])] + [numbers[-1]]
# Tests
numbers = [1, 2, 3]
delimiters = [4, 4, 2, 4]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 2, 4, 3] + ['4', 4, 2, 4, 3] + [4]
print(result)
```