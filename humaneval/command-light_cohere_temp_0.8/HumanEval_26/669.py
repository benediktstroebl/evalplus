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
This function removes duplicate numbers from the input list and returns a new list with unique numbers. The function uses a set data structure to keep track of the seen numbers and ensures that each number is unique.

This solution is self-contained and can be used as a standalone function to solve the given problem.