```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
# sample test
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
```