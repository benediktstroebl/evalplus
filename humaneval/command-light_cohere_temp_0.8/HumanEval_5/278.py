```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim in zip(numbers, [delimeter] * 2)]

# Test the function with sample inputs and assertions
numbers = [4, 2, 3]
assert intersperse(numbers, 4) == [5, 4, 2, 4, 3]

numbers = [1, 2, 3]
assert intersperse(numbers, 4) == [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4]
assert intersperse(numbers, 4) == [1, 4, 2, 4, 3]

numbers = [10, 20, 30]
assert intersperse([10, 20, 30]) == [10, 10, 20, 10, 20, 30]
```