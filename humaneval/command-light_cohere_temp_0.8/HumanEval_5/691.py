```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i < len(numbers) - 1:
            result.append(num + delimeter)
        else:
            result.append(num)
    return result
```
This script provides a self-contained solution for the problem described, where it inserts the `delimiter` between every two consecutive elements in the input list.