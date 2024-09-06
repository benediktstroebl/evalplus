```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 4, 8]
result = intersperse(numbers, delimiters)

print(result)  # Expected output: [1 4 8 2 4 8 3]
``` 
This script provides a self-contained solution to the problem.