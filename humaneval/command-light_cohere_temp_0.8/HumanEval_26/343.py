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
This code implements a remove_duplicates function that takes a list of integers as input and removes all duplicate elements. It uses a `set()` to create a set of unique integers from the list, then iterates through the list and adds each integer to the set if it's not already present. Finally, it returns a set as the list of unique integers.