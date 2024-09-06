```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[::-1]

# Test cases
numbers = [1, 2, 3, 4, 5]
delimiter = 4
expected = [1, 4, 2, 4, 3, 5]

print(expected)
print(intersperse(numbers, delimiter))
```