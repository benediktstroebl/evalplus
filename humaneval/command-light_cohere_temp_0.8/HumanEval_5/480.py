```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n, delimeter+1) for n in numbers

# Test cases
numbers = [1, 2, 3, 4, 5]
delimiter = 3
expected = [1, 3, 4, 5, delimiter, 2, 5]
print(intersperse(numbers, delimiter))  # Output: expected
```