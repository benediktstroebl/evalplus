```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', 'hello world'], 'l')
    ['hello world']
    """
    return [x for x in strings if x.startswith(prefix)]
```

This function uses a list comprehension to filter the strings in the input list, only keeping those that start with the specified prefix.