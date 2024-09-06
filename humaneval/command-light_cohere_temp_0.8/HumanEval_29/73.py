```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python code defines a function `filter_by_prefix` that filters an input list of strings, returning a new list containing only those strings that start with the given `prefix`. The function uses the `startswith` method of the strings' string class to check if each element's prefix matches the given `prefix`.