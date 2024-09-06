```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that filters an input list of strings to only those starting with a specific prefix. It uses the `startswith()` method to check if a given string starts with a specific prefix.