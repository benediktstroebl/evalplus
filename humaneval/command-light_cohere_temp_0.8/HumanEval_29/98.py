```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function **filter_by_prefix** that filters an input list of strings and returns a new list containing only the elements that start with the specified prefix. The test cases are provided to verify the correctness of the function.