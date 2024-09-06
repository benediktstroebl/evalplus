```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that filters an input list of strings to include only those that start with a specified prefix.  It uses the process like `filter` to iterate over each string and check if it starts with the given prefix.