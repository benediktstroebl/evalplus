```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code takes advantage of list comprehension to filter strings in the list that contain the given substring. It thereby succinctly achieves the goal stated in the original problem.