```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script provides a function `filter_by_prefix` that filters an input list of strings and returns only the ones that start with the given `prefix`.