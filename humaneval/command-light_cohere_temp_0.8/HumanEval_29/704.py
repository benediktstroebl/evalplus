```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a `filter_by_prefix` function that filters an input list of strings to return only those that start with the given `prefix`. The function uses the `startswith` method to check if each string in the list starts with the given `prefix`.