```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
This function uses a set to keep track of seen numbers, then iterates through the input list, adding each number to the set if it hasn't been seen before. This ensures that each number only appears once, and any duplicates are removed. 

The function is well-contained, and does not require any additional variables or external calls. It can be used as a problem of removing duplicates from an input list of integers.