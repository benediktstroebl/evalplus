```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim in zip(numbers, [delimeter] * 2)]

# Test the function with various input cases
numbers = [1, 2, 3, 4]
print(inperse(numbers, 2))  # Expected output: [1, 2, 3, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
print(inperse(numbers, 2))  # Expected output: [1, 3, 5, 2, 4, 5]

numbers = [10, 20, 30, 40]
print(inperse(numbers, 10))  # Expected output: [10, 20, 30, 40]

numbers = [10, 10, 20, 10, 30]
print(inperse(numbers, 20))  # Expected output: [10, 10, 30, 10, 20]
```