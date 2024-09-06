```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. The function returns a filtered list of strings that start with the specified prefix. This function is a single pass and does not require any external imports.