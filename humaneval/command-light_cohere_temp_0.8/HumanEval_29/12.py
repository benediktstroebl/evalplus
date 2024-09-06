Here is a self-contained Python script with a function that filters an input list of strings for those that start with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

The function `filter_by_prefix` takes a list of strings `strings` and a prefix `prefix` as input, and returns a new list containing only the strings that start with the given prefix.