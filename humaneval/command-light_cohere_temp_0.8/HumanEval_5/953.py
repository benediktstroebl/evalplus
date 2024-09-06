```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Unit tests for the function
numbers = [1, 2, 3]
delimiters = [4, 4, 4]

result = intersperse(numbers, delimiters)
print("Result:", result)

# Test for empty list
print("Test with empty list:", intersperse([], delimiters))

# Test with one element
numbers = [4]
print("Test with one element:", intersperse(numbers, delimiters))
```