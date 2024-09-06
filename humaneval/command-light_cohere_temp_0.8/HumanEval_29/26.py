```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix
    Returns: filtered list of strings starting with the given prefix
    """
    return [x for x in strings if x.startswith(prefix)]
```
This Python code defines a function `filter_by_prefix` that filters an input list of strings, returning a new list containing only those strings that start with a specified prefix.