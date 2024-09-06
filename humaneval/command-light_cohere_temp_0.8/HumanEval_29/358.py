```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This code implements a function `filter_by_prefix` that filters an input list of strings, returning only those that start with a specified prefix. It utilizes the common Python list comprehension with a generator expression to create a new list with the desired prefix.