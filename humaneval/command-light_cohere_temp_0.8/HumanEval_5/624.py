```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n, delimeter + n  for n in numbers)

#unit tests
numbers = [1, 2, 3, 4, 5]
delimiters = [1, 2, 3, 4, 5]
result = intersperse(numbers, delimiters)
shouldBe = [1,1,2,2,3,3,4,4,5,5]

print(result == shouldBe)
```