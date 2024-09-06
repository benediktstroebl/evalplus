```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 2) + numbers[::-1]

# Test case 1: Basic operation
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 2, 4, 3]

# Test case 2: Empty input list
numbers = []
result = intersperse(numbers, 4)
print(result)  # Expected output: []

# Test case 3: Single element list
numbers = [1]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 1]

# Test case 4: List with duplicates
numbers = [1, 2, 2, 3]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 2, 4, 3]

# Test case 5: Complex list
numbers = [1, 2, 3, 4, 5, 6]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 2, 4, 3, 5, 6]
```
This script defines a function `intersperse` that, given a list of numbers and an integer `delimiter`, returns a new list with the given delimiter between every second element of the input list, and the original list reversed at the end.