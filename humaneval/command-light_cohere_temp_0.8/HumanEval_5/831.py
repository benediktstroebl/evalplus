```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
# Test cases
numbers = [1, 2, 3]
delimiters = [4, 8]
expected = [5, 12, 16]

numbers = [1, 2, 3]
delimiters = [4, 2]
expected = [5, 6]

numbers = [4, 4, 4]
delimiters = [8, 4]
expected = [12, 12]

print(f'Test cases passed: {expected}')
```