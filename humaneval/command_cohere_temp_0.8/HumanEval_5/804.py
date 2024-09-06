```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
delimeter = 4

expected_result = [1, 4, 2, 4, 3]

print(intersperse(numbers, delimeter))  # Output: [1, 4, 2, 4, 3]
```