```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```

This well-optimized code uses Python's built-in `set` data type, which removes duplicate elements and converts the set back to a list to return the result. It does not require any additional variables to maintain the order of elements, making it an efficient one-liner that effectively solves the problem. 

This approach ensures that duplicates are instantly removed without requiring any additional computations or maintenance of an ordered list.