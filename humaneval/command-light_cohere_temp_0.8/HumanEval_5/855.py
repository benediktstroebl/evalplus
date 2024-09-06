```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimiter)
        result.append(num)
    return result
# test case 1
numbers = [4]
result = intersperse(numbers, 4)
print(result)

# test case 2
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)
```