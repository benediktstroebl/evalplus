```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize set to store unique elements
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique elements from the input. The function uses a set data structure to keep track of elements that have already been seen and then adds any new element to the list if it has not been seen before. The function effectively removes duplicate elements from the input list and returns the updated list.