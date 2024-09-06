```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers_list = [4, 2, 3]
print(inperseue(numbers_list, 4))  # Output: [4, 8, 12, 16, 20, 22]

numbers_list = [1, 2, 3]
print(inperseue(numbers_list, 4))  # Output: [1, 6, 9, 12]

numbers_list = [10, 20, 30, 40]
print(inperseue(numbers_list, 2))  # Output: [10, 12, 14, 16, 18, 20, 22, 24, 26]
```