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
This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list that contains unique integers from the original list. The code uses a set to keep track of the unique integers and a list comprehension to filter out duplicates.