```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [num] + [num] + [delimeter] * (len(numbers) - 2) + [num]
    return result

# Test the function with various inputs
numbers = [1, 2, 3, 4, 10, 2]
delimiters = [0, 4, 8, 12, 16]  

expected = [1, 4, 2, 4, 8, 10, 12, 16]

print(f"Expected: {expected}")
print("\nGot:", intersperse(numbers, delimiters))

```