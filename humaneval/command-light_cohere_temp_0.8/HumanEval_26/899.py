```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [num]
```
This code implements a function called remove_duplicates that takes a list of integers and returns a new list with no duplicates. The function uses a set to keep track of elements that have been encountered, then iterates through the input list, appending elements to the result list if they haven't been seen before. If a element has been seen before, it is added to the seen set.

This approach ensures that duplicate elements are effectively removed from the input list, resulting in a unique list of integers. The code is self-contained and concise, effectively solving the problem of removing duplicates from an input list of integers.