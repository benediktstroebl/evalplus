```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n, delimeter + n) for n in numbers
numbers_test = [1, 2, 3, 4, 5]
print(intersperse(numbers_test, 4))  # expected output: [1, 4, 2, 4, 3, 5]
```