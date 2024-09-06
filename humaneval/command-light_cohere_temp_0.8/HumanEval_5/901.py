```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers = [1, 2, 3, 4]
delimiters = [2, 3]
result = intersperse(numbers, delimiters)

print(result == [3, 5, 1, 6, 2, 8])  # Should print True
print(result == [0, 4, 7, 10])  # Should print True
print(result == [1, 2, 3, 4, 5])  # Should print False
```