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

The approach used is a mixture of a loop and set manipulation. This allows us to keep the complexity at O(n) while keeping the implementation concise.

The loop iterates over the input list. For each element, it checks whether it is already in the 'seen' set. The set only stores a single instance of any element, so if an element is in the set, it has been seen before. If an element is not in the set, it has not been seen yet, so we add it to both the set (to mark it as seen) and the result list.

This ensures that any element that occurs more than once in the input list will only appear once in the output list. And elements that are only seen once will be preserved and remain in the same order as in the input.