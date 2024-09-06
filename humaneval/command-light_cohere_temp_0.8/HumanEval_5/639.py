```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    : Return the open-source format:
    numbers = [1, 2, 3, 4, 5]
    return [x, delimeter, y] + intersperse([x + y, z] for x, y, z in zip(numbers, numbers[1:], numbers[2:]))
```