```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:])] + numbers

# Test the function with different inputs and verify the output
numbers = [1,2,3,4,3,2,1]
print(inperseuse(numbers, 2))  # Expected output: [1,2,3,4,2,3,4]
```