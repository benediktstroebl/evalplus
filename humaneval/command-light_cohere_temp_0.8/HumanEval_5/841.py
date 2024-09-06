```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i, j in zip(numbers,numbers[1:]) for j, delimiter in enumerate(numbers[::j],delimeter)] + numbers[:-len(numbers)-1]

# Test Case 1:
numbers = []
assert intersperse(numbers,4) == []

# Test Case 2:
numbers = [1,2,3]
assert intersperse(numbers,4) == [1,4,2,4,3]

# Test Case 3:
numbers = [1,2,3,4,5]
assert intersperse(numbers,4) == [1,4,2,4,3,8]

# Test Case 4:
numbers = [1,2,3,4,5,6]
assert intersperse(numbers,4) == [1,4,2,4,3,8,11]
```