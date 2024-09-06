A Python script that solves the given problem is:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The `filter_by_prefix` function filters a list of strings, returning only those that start with the specified prefix. It uses the essential list comprehension, which is a powerful tool in Python for looping through iterators.