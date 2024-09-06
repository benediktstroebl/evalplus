```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix` that filters an input list of strings, denoted by `strings`, and returns a new list containing only those strings that start with the specified `prefix`. The function uses the `startswith` method of the string class to check if each element of the input list starts with the given `prefix`.