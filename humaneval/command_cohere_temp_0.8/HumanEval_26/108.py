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

The algorithm is a typical use of sets to identify unique elements in a collection. The set `seen` will contain all numbers that were previously seen. Each number from the input list is checked if it is already in the set. If it is not, it is added to the set and also to the result list. If it is, we check if it was the only occurrence of a number, and if so, we also add it to the result. The output of the provided test case is `[1, 3, 4]`.