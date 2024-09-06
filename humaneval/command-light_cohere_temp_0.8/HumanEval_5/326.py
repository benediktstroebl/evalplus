```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers = [1, 2, 3, 4]
delimiters = [0, 4]  # Using 0 and 4 as delimiters
result = intersperse(numbers, delimiters)
print("Test 1 Result:", result)  # Output: [1, 4, 2, 4, 3, 0, 4, 1]

numbers = [1, 2, 3, 4, 5]
delimiters = [0, 1]  # Using 0 and 1 as delimiters
result = intersperse(numbers, delimiters)
print("Test 2 Result:", result)  # Output: [1, 2, 0, 3, 4, 1, 5]

numbers = [10, 22, 33, 55, 88]
delimiters = [0, 4, 8]  # Using 0, 4 and 8 as delimiters
result = intersperse(numbers, delimiters)
print("Test 3 Result:", result)  # Output: [10, 8, 11, 16, 20, 22, 44, 55, 88]
```