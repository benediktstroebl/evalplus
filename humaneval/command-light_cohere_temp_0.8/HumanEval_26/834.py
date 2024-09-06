```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return thereturn
```

This function uses a set to keep track of numbers it has seen before. It then iterates through the the numbers, adding each unique number to the result list.