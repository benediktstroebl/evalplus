```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)

# Check the result against the expected output
assert list(result) == [1,4,2,8,3]
```