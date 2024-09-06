```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
# Test case: concatenate numbers with a specified delimiter
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]
result = intersperse(numbers, delimiter)
assert list(expected) == result
```