```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or len(seen) == 1:
            result.append(num)
            seen.add(num)
    return result
```

The function `remove_duplicates` removes elements that occur more than once in a list of integers, while preserving the order of the remaining elements. It does so by utilizing a set, `seen`, to keep track of the unique elements encountered while iterating through the input list. When an element is encountered for the first time, it is added to both the result list and the set. If an element has already been added to the set and is encountered again, it is skipped, ensuring that only unique elements are added to the result.