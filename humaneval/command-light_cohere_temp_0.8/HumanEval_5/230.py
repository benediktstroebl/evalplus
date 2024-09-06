```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + j for i, j in zip(numbers, numbers[1:])] + numbers

# Test cases
numbers = [1, 2, 3, 4, 5]
print(inperseple([1, 2, 3], 2))  # Expected: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 3, 5]
print(inperseple([1, 2, 3], 3))  # Expected: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4]
print(inperseple([1, 2, 3], 2))  # Expected: [2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6]
print(inperseple([1, 2, 3], 2))  # Expected: [1, 3, 4, 5, 6]
```