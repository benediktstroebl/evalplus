```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n+delimiter for n, delimiter in zip(numbers, delimeter*[::repeat(delimiter)][-1:])))

# Unit tests
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)
shouldBe = [1, 4, 2, 4, 6, 3, 10, 5]
assert list(result) == shouldBe

numbers = [6,3,2]
delimiters = [1,4]
result = intersperse(numbers, delimiters)
shouldBe = [6, 1, 8, 3, 2]
assert list(result) == shouldBe
```