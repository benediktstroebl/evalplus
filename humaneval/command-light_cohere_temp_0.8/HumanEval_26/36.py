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

The function uses a set data structure to track previously seen numbers, then iterates through the input list, adding numbers to the set if they haven't been seen before. If a number has already been seen, it is added to the result list.