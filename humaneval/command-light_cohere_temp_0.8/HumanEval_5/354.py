```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[1:]

# Test cases
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]

print(intersperse(numbers, delimiter)) == expected
```