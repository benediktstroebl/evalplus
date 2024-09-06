```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)]

# Test the function with a list of numbers and a delimiter
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Expected output: [1, 4, 2, 4, 3]

# Test the function with empty list
numbers = []
result = intersperse(numbers, 10)
print(result)  # Expected output: []

# Test the function with single number
numbers = [1]
result = intersperse(numbers, 10)
print(result)  # Expected output: [1, 10]
```