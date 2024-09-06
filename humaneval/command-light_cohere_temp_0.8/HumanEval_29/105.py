Here is a self-contained Python script that solves the problem of filtering strings by their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function, `filter_by_prefix`, that takes in a list of strings and a prefix as input, and returns a new list that contains only the strings from the original list that start with the given prefix. 

The `startswith` method from Python's string module is used for this filter.