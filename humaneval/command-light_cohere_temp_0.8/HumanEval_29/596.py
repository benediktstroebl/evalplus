```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function employs the Python list comprehension and the starts with operator to filter the input list of strings. It returns a filter based on the given prefix.