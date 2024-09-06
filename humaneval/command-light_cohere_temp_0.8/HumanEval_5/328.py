```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        result.append(n) if i != 0 else delimeter
    return result
# Test the function with an empty list and a few numbers
test_result = intersperse([], 4)
assert test_result == []
test_result = intersperse([1, 2, 3], 4)
assert test_result == [1, 4, 2, 4, 3]
test_result = intersperse([10, 20, 30, 40])
assert test_result == [10, 20, 30, 40, 10, 20, 30, 40]
```