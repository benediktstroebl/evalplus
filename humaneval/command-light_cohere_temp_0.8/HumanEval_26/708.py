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
```
This function removes duplicates from the list of integers, then returns a new list.

The function uses the set data structure to quickly identify duplicate elements and then adds each number to the result list only if it has not been seen before.