```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)] + [num + delimeter for num in numbers[1:] :]

# Unit tests
numbers = [1, 2, 3]
delimiters = [0, 4]

assert intersperse(numbers, delimiters) == [1, 4, 2, 4, 3]
assert list(numbers[1::::neighbors(2))) == delimiters
```