Here's the self-contained Python function that solves the problem:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [num]
```

This function uses a set to keep track of unique numbers, then adds the number to the result if it's not already in the set. The function also returns a unique list of integers.