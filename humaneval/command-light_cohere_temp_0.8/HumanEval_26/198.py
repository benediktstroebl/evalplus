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
This Python code defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The function utilizes a `set` data structure to track seen elements and creates a new list with unique integers. The `seen` set is initially empty, and the function iterates through the input list, appending elements to the `result` list if they are not already in the set. The function then returns the result list, effectively removing duplicate elements.