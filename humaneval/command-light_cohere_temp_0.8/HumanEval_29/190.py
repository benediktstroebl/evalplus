```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

The provided code defines a function named `filter_by_prefix` that takes two arguments: a list of strings (`strings`) and a prefix string (`prefix`). It returns a new list containing only the strings from the input list that start with the given prefix. This function effectively filters the also out all strings that don't have the specified prefix at the beginning.