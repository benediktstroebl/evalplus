```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list."""
    result = []
    for i, n in enumerate(numbers):
        if i != 0 and i < len(numbers) - 1:
            result.append(delimiter)
        result.append(n)
       
    return result
```