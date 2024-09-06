```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Unit tests
numbers = [1, 2, 3, 4]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)
print(result)  # Expected Output: [1, 0, 4, 2, 4, 3, 0, 4]
```