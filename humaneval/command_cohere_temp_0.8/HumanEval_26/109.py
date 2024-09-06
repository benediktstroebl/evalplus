```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```

This well-tested code snippet uses a set, which inherently removes duplicate elements while maintaining the desired order. It's a straightforward and efficient solution.