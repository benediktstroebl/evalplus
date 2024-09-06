```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [4, 12, 8, 10, 6]
result = intersperse(numbers, 4)
print(result)  # Expected Output: [4, 8, 12, 10, 16, 6]

numbers = [1, 2, 3, 4, 5, 6, 7]
result = intersperse(numbers, 3)
print(result)  # Expected Output: [1, 4, 7, 5, 6, 10, 3]
```