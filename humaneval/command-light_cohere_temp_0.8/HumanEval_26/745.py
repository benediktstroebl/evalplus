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
This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with unique integers from the input. The code uses a set data structure to keep track of numbers that have been seen before, and it iterates through the input list, appending any integer that is not already in the set to a new list. 
The code provides a self-contained solution for the problem of removing duplicate elements from a list of integers.