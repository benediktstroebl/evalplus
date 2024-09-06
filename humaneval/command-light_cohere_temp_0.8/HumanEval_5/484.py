```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        if i > 0: result.append(delimeter)
        result.append(n)
   return result

# Testing the function
numbers = [1, 2, 3,4,3,2]
result = intersperse(numbers, 2)
print(result)
# Expected Output: [1, 2, 3, 2, 4, 3]
```