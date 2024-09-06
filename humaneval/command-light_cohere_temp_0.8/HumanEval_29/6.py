Here is a self-contained Python script that solves the problem of filtering strings based on their prefixes:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function, `filter_by_prefix`, that takes a list of strings and a prefix as input and returns a new list of strings that start with that prefix. 

The function uses the list comprehension to filter out the strings that do not start with the given prefix.