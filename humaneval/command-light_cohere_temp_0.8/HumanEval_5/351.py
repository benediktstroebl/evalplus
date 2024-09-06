```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim in zip(numbers, [delimeter]*2)]

# Test the function with different inputs and assertions
numbers = [4, 1, 9, 2, 3]
assert intersperse(numbers, 4) == [5, 4, 6, 4, 9, 4, 2, 4, 3]

numbers = [1, 2, 3]
assert intersperse(numbers, 4) == [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
assert intersperse(numbers, 4) == [1, 4, 2, 4, 3, 5]

numbers = [1, 2, 3, 4, 6]
assert intersperse(numbers, 4) == [1, 4, 2, 4, 5, 4, 6]

numbers = [1, 2, 3, 4, 7]
assert intersperse(numbers, 4) == [1, 4, 2, 4, 3, 7, 4]
```