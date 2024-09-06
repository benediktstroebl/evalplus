```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a `filter_by_prefix` function that filters an input list of strings, returning only those that start with a specified prefix. 
It uses the `startswith` method to achieve this.