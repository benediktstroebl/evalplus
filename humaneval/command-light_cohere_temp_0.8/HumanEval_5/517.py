```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list."""
    result = [num] + [num + delimiter for delimiter in range(delimeter)] + [num] 
    return result[:] 

# Test case 1
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert list(result) == [1, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3]
result = intersperse(numbers, 100)
assert list(result) == [1, 100, 2, 100, 3]

# Test case 3
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 2)
assert list(result) == [1, 2, 4, 5, 3]
```