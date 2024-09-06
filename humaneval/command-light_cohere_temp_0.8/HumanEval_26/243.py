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
This script defines a function called remove_duplicates that takes a list of integers as input and returns a new list with all distinct integers. It uses a critical technique to guarantee that no duplicates are added to the result list by using a set to keep track of elements that have been seen before. 

This function is a self-contained solution to the problem of removing duplicate integers from a list.