```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. It uses the `startswith` operator to filter the list of strings and only returns the ones that start with the given prefix. This function is useful for tasks that require the filtering of strings based on a prefix.