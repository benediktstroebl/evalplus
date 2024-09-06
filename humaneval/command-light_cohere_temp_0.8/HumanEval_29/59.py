```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It uses the method `startswith` from Python's string module to filter the strings in the list that start with the given prefix.