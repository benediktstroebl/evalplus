```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list"""
    result = [num for i, num in enumerate(numbers) if i % 2 == 0] + [delimeter] + [num for i, num in enumerate(numbers) if i % 2 == 1]
    return result

# Test cases
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 3)
print(result)  # expected output: [1, 3, 2, 4, 5]
numbers = [1, 2, 3, 4, 5, 6]
result = intersperse(numbers, 4)
print(result)  # expected output: [1, 4, 6, 2, 5]  6, 5]
```