Here is a self-contained Python script with a function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script provides a function `filter_by_prefix` that filters an input list of strings, only keeping those that start with the specified prefix.