Here's the solution:
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
This script defines a function called remove_duplicates that takes a list of integers as input and returns a new list with all distinct integers. The function uses a set data structure to keep track of the integers that have already been seen, and it iterates through the input list, appending only the integers that have not been seen before. The use of the set() function ensures that each integer is only added to the set once, eliminating duplicate entries.