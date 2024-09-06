Here's a self-contained Python script that implements the function filter_by_prefix from the previous prompt:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix."""
    return [x for x in strings if x.startswith(prefix)]
```

This code provides a simple and self-contained solution to the problem. It uses list comprehension and a starts with the prefix checking condition, which returns a list of strings that start with the specified prefix.