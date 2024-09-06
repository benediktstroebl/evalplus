```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [num]
    for i in range(1, len(numbers)):
        result.append(numbers[i] + delimeter)
    result.append(numbers[0])
    return result

# Test case:
numbers = [1, 2, 3, 4, 5]
delimiter = 4
expected = [1, 4, 2, 4, 3, 5]
print(f"Result: {expected}")
```