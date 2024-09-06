```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once from the input list.
    Input:
    numbers = [1, 2, 3, 2, 4]
    Output: [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```