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

This function, `remove_duplicates`, takes a list of integers as input and returns a new list with no duplicates. It uses a set to keep track of numbers that have been seen, and then adds any number to the result list if it hasn't been seen before.