```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function `filter_by_prefix` that filters a list of strings, returning a new list containing only those that start with the specified prefix. It uses the specific typing to provide better static type checking and more readable variable names.