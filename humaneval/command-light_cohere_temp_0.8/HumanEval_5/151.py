```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]
    return result

# Test case 1
numbers = [4, 2, 3]
result1 = intersperse(numbers, 4)
print(result1)  # Expected output: [4, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3]
result2 = intersperse(numbers, 4)
print(result2)  # Expected output: [1, 4, 2, 4, 3]

# Test case 3
numbers = [1, 2, 3, 4]
result3 = intersperse(numbers, 2)
print(result3)  # Expected output: [1, 2, 2, 3, 4]
```