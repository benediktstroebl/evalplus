Here is a self-contained Python script that solves the problem you have described:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script provides a function `filter_by_prefix` that filters an input list of strings, only keeping those that start with the given prefix.