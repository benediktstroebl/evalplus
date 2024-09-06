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
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all unique integers. The function uses a set data structure to keep track of the integers it has encountered, then iterates through the input list, adding each integer to the set and the result list if it is not already present in the set. 

This self-contained function can be used to efficiently remove duplicates from any list of integers.