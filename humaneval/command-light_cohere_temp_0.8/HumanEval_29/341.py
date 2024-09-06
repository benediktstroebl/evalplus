```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses a list of strings and a prefix to filter and return a new list with all the elements that start with that prefix.