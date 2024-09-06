```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix."""
    return [x for x in strings if x.startswith(prefix)]
```
This Python code defines a function called `filter_by_prefix` that filters a list of strings. It takes two input arguments: a list of strings and a prefix. the function returns a strings that start with the given prefix.