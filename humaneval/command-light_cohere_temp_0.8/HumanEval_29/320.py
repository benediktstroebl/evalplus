```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python code defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses the string `startswith` method to check if each string in the list starts with the provided prefix. The function returns a filtered list of strings that match the given prefix.