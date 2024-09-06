```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    Return list of strings that start with the given prefix.
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]
```

The function filters a list of strings, only keeping the ones that start with a specific prefix. It uses the prefix parameter to define the prefix and returns a new list with the matching strings.