Here's a self-contained Python script with a function that filters strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix.