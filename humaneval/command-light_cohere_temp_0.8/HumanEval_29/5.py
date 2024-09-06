```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function called `filter_by_prefix` that filters an input list of strings based on whether they start with a specified prefix. The function uses the filtering technique to return only the strings that start with the given prefix.