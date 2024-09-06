```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. This is accomplished via a list comprehension, using a generator expression to create a new list that includes only the matching strings. To ensure compatibility with the specified typing module, the type of the return value is specified as `List[str]` as well.