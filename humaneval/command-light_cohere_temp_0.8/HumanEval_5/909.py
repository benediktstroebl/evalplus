```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
# Test the function with sample inputs
numbers = [1, 2, 3, 4]
delimiters = [4, 4, 8, 12]
result = intersperse(numbers, delimiters)
shouldBe = [1, 4, 8, 16, 24, 32]

print(result == shouldBe)  # True if the function works correctly
```