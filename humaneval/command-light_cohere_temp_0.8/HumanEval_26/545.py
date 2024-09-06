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
This function removes duplicate numbers from a list and returns the modified list. The function utilizes a set data structure to keep track of seen numbers, and then iterates through the input list, appending only unique numbers to the result list.