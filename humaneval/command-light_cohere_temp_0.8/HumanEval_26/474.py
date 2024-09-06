Here's a self-contained Python function that removes duplicates from a list of integers:
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

This function uses a set to keep track of seen numbers, then iterates through the input list. It adds any number to the set if it hasn't been seen before, and adds it to the result list.