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
This function removes duplicates from the input list of integers and returns a new list with unique integers. It uses a `set()` to keep track of integers that have already been seen, and then it adds any new integer to the result list if it hasn't been seen before.