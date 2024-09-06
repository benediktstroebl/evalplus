```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the filter method with a generator expression to create a new list with elements that start with the given prefix. 

This is a self-contained solution to the problem of filtering strings with a given prefix.