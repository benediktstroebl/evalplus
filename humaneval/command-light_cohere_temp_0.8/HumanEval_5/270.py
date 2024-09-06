```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [num] + [num] + [delimeter] * (len(numbers) - 2) + [num]
    return result[:]
# Test the function with different inputs
numbers = [1, 2, 3]
print(intersperse(numbers, 4))  # Expected output: [1, 4, 2, 4, 3]
numbers = [1, 2, 3, 4]
print(intersperse(numbers, 3))  # Expected output: [1, 2, 3, 4]
numbers = [1, 2, 3, 5]
print(intersperse(numbers, 2))  # Expected output: [1, 2, 3, 5]
numbers = [10, 20, 30]
print(intersperse(numbers, 10))  # Expected output: [10, 20, 30]
```