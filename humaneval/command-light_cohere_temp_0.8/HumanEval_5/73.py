```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + j for i, j in zip(numbers, numbers[1:]+[delimeter])]

# Test cases
numbers = [1, 2, 3]
print(intersperse(numbers, 2))  # Expected output: [1, 2, 3, 2, 3]

numbers = [4, 5, 6]
print(intersperse(numbers, 2))  # Expected output: [4, 6, 5, 6]

numbers = [10, 20, 30]
print(intersperse(numbers, 2))  # Expected output: [10, 12, 14, 16, 18]

numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 6))   # Expected output: [1, 2, 3, 4, 5, 6]
```
This script defines a function `intersperse` that separates consecutive elements in a list by a specified `delimiter`. It also provides several test cases to validate the function's behavior.