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
This Python function, `remove_duplicates`, takes a list of integers as input and returns a new list with unique integers. The function uses a set to keep track of integers that have been seen before and removes duplicate elements from the input list.