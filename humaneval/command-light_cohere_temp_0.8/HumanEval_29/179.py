Here is a self-contained Python script that solves the problem of filtering strings that match a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script provides a function called `filter_by_prefix` that accepts a list of strings and a prefix as arguments. The function uses the string starting check to filter the list and return only the strings that start with the given prefix.