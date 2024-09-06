```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
delimeter = 4

expected_result = [1, 4, 2, 4, 3, 4, 5]

assert intersperse(numbers, delimeter) == expected_result
```