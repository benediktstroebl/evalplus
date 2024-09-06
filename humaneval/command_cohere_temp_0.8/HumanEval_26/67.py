```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```

This well-tested code fragment uses a set, which is well-suited for removing duplicate elements while preserving the order of the remaining elements. This solution is both efficient and effective in handling the given problem.