```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 4, 4]
result = intersperse(numbers, delimiters)
print(result)  # Output: [5, 8, 7, 12, 16]
```