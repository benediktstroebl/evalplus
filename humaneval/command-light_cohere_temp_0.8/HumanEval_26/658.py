```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ 
    Removes elements that occur more than once from the input list.
    Returns a guaranteed unique list of integers.
    """
    detailed test cases: 
    1. [1, 2, 3, 2, 4] -> [1, 3, 4]
    2. [1, 1, 2, 2, 3] -> [1, 2, 3]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
Do you require any further assistance with this code?