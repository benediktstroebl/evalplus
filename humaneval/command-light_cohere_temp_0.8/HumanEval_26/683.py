Here is a self-contained Python function that solves the problem you described: 

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

This function takes a list of integers as input and creates a set of all the distinct numbers in the list. Then, it creates a new list that contains all the numbers in the original list that are not already in the set.