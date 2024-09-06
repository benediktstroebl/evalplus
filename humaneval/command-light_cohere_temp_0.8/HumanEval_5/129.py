```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers[:2] + [delimeter] + numbers[2:]

# Test case 1
numbers = [4, 2, 3]
test_result = intersperse(numbers, 4)
assert list(test_result) == [4, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3]
test_result = intersperse(numbers, 4)
assert list(test_result) == [1, 4, 2, 4, 3]

# Test case 3
numbers = [1, 2, 3, 4, 5]
test_result = intersperse(numbers, 4)
assert list(test_result) == [1, 4, 2, 4, 3, 4, 5]
```