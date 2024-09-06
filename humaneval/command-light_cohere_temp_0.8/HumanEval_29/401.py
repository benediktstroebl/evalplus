```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

The filter_by_prefix function filters a list of strings, taking a list of strings and a prefix as input, and returns a new list that includes only the strings that start with the given prefix. The function uses the filtering by using the startswith operator, which checks if a string starts with the given prefix.