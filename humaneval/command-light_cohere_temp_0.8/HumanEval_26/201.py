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

This function, `remove_duplicates`, takes a list of integers as an argument and returns a new list with all integers unique to the input list. The function uses a set data structure to keep track of the integers that have been seen before, and then adds any integer to the result list if it has not already been seen.