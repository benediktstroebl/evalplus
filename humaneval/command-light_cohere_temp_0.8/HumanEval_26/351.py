Here's the solution:
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

This function uses a set data structure to keep track of the numbers it has seen so far, and then only adds the number to the result list if it hasn't been added to the set before.