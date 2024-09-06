```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
```
The function `remove_duplicates` takes a list of integers and removes all duplicate elements. It uses a`set` to keep track of seen elements and creates a new list with unique elements.