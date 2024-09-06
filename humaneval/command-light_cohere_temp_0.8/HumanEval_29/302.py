```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This code implements a function `filter_by_prefix` that filters an input list of strings, returning a new list that includes only those that start with the given prefix. 

The function uses the `startswith` method to check if each string in the input list starts with the given prefix.