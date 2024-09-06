```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It returns a The list of strings from the input list that start with the given prefix. The function is self-contained, and it passes the corresponding tests.