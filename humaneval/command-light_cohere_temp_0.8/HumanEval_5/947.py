```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[1:]

# Test cases
numbers = [1, 2, 3]
delimiters = [0, 4]

# Function call and expected result
result = intersperse(numbers, delimiters)
print(result)  # Expected output: [0, 4, 2, 4, 3, 0, 4, 3]
```