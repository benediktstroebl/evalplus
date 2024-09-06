```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```

This well-optimized code uses Python's built-in `set` data type, which removes duplicate values from a collection and then converts this set back to a list to return the result. It is the most efficient and concise solution.