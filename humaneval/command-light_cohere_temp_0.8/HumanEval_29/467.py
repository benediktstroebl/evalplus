```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes in a list of strings and a prefix, and returns a new list that contains only the strings from the original list that start with that prefix. The `istart requires is passed a list of strings and a string, and the return is a list of strings that match the given prefix.