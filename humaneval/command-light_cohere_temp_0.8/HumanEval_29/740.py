Here is a self-contained Python script with a function that filters strings by their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script provides a function that takes in a list of strings and a prefix, and returns a new list that contains only the strings from the input list that start with that prefix.