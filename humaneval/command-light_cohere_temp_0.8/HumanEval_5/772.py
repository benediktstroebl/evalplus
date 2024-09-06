```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[1:]

# Test case 1: Basic Test
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Expected output: [1, 4, 2, 4, 3]

# Test case 2: Empty input list
numbers = []
result = intersperse(numbers, 5)
print(result)  # Expected output: []

# Test case 3: Single element list
numbers = [5]
result = intersperse(numbers, 3)
print(result)  # Expected output: [5, 5, 5]

# Test case 4: Lists with different lengths
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 2, 4, 3]
```
This Python function, `intersperse`, is designed to separate elements of an input list by a specified delimiter, resulting in a new list with proper spacing. This is ensures that the code is self-contained, and it can be used as a standalone function with various test cases.