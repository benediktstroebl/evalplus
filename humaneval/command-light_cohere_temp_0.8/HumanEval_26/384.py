Here's the solution for your markdown code block:

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

The `remove_duplicates` function takes a list of integers as input and returns a new list containing only the unique integers. The function uses a set to keep track of integers that have been seen before, and then it iterates through the input list, adding each integer to the set and appending it to the result list if it is not already in the set.