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
This code defines a function `remove_duplicates` that takes a list of integers and returns a new list with all integers unique in the input list. It utilizes a set `seen` to keep track elements that have already been seen and a new list `result` to collect the remaining, unique integers.