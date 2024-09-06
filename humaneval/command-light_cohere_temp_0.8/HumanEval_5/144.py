```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Unit tests
numbers = [1, 2, 3]
delimiters = [4, 8]

expected = [1, 4, 8, 2, 12, 3, 16]

print("Test 1:", expected == intersperse(numbers, delimiters))
print("Test 2:", numbers == intersperse(numbers, 10))
print("Test 3:", intersperse(numbers[:-], delimiters) == numbers[1:]))
```