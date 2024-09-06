```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [str for str in strings if str.startswith(prefix)]
```

The function uses a generator expression to filter the strings in the list, only keeping the ones that start with the specified prefix.