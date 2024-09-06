```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 4))  # [1, 4, 2, 4, 3, 4, 5]

empty_list = []
print(intersperse(empty_list, 4))  # []
```