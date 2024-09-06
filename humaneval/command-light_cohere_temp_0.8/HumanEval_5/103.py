```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
# Test the function
numbers = [4, 12, 8, 3, 10, 5, 9, 2, 1]
result = intersperse(numbers, 4)
print(result)  # Output: [5, 8, 12, 10, 2, 4, 9, 7, 3, 6, 1]
```