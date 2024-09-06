```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function named `filter_by_prefix` that takes a list of strings and a prefix as input. The function returns a filter the list of all the strings from the input list that start with the given prefix.