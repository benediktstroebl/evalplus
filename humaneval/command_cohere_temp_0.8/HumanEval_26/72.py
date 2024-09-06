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

The approach used in the function `remove_duplicates` is to iterate over the input list of integers, and for each number, add it to both the resulting list and a set. The set `seen` is used to keep track of all unique elements seen so far, fulfilling the requirement to remove elements that occur more than once in the original list. If a number is encountered that is not in the set, or if the set contains only one element, it means that it's the first or second occurrence of this number, and therefore it is added to the result and the set. Using a set for tracking unique elements ensures efficient duplicate detection.