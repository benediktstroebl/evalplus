A solution using a list comprehension and string starting prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The `filter_by_prefix` function filters a list of strings using the `startswith` method, which returns `True` if the string starts with the given prefix.

The function then returns a new list containing only the strings that match the given prefix.