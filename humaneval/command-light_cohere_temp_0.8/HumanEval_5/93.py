```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n+(n+delimeter) for n in numbers)

# Test the function
numbers = [1, 2, 3]
print(intersperse(numbers, 4))  # Expected output: [1, 4, 2, 4, 3]
``` 
I hope this provides a complete, self-contained solution to the problem described.