Here is a self-contained Python function that solves the problem of removing duplicates from a list of integers:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [result]
    return result
```

This function takes a list of integers as input and uses a set to keep track of duplicate values. The function then iterates through the list, checking each value against the set, and adds the unique values to a new list. The function returns this list containing only the unique values.