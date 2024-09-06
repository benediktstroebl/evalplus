```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim in zip(numbers, [delimeter]*2)]

# Test case 1
numbers = [4, 3, 2, 1]
result = intersperse(numbers, 4)
assert list(result) == [4, 4, 2, 4, 3, 4]

# Test case 2
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert list(result) == [1, 4, 2, 4, 3]

# Test case 3
numbers = [4, 3, 2, 1]
result = intersperse(numbers, 5)
assert list(result) == [4, 5, 2, 5, 3, 5]

# Test case 4
numbers = [1, 2, 3]
result = intersperse(numbers, 5)
assert list(result) == [1, 5, 2, 5, 3]
```

This script defines a function `intersperse` that inserts a `delimiter` value between every two consecutive elements in the input list. The function is tested through a series of test cases to ensure its correctness.