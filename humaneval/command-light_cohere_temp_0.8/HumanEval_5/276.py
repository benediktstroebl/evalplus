```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[1:] 

# Test the function with different inputs and verify the expected output
numbers = [1, 2, 3]
delimiters = [4, 4, 2, 4]
print(intersperse(numbers, delimiters))  # Expected output: [1, 4, 2, 4, 3, 4, 2, 4]
```