Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings that start with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that filters an input list of strings to return only those that start with a given prefix. The function uses the filter operation to check if each string starts with the specified prefix, and then returns the filtered list.