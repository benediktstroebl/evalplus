```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num) + delimeter
    result.append(num)
    return result
# test cases:
print(inperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(inperse([1, 2, 3], 100))  # []
print(inperse([1, 2, 3], -1))    # []
print(inperse([1, 2, 3], 0))    # [1, 2, 3]
print(inperse([2, 3, 4], 5))    # [2, 3, 5, 4]
```