```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

The filter_by_prefix function takes a list of strings and a prefix as input and returns a new list that contains only the strings that start with that prefix. It uses the string.startswith to check if a string starts with the given prefix.