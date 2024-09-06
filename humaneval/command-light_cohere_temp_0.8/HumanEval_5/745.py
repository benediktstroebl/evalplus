```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 4, 8, 16]

result = intersperse(numbers, delimiters)

# Verify result
assert len(result) == len(numbers)
assert all(result == [1, 4, 8, 16, 2, 4, 8, 16, 3])  # This is a tricky one...

print("Test passed!")
```