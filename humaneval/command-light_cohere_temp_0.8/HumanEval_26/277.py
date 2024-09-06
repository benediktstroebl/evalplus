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
This script defines a function `remove_duplicates` that removes duplicate numbers from a list. It uses a set to keep track of seen numbers and then iterates through the input list, appending numbers to `result` only if they are not already in the set.