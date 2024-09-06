```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that filters an input list of strings to include only those that start with a given prefix.  The function uses the Python's `startswith` method to check if a string starts with a given prefix.