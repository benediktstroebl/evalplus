```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', '123', 'array'], 'a')
    ['abc', '123']
    """
    return [s for s in strings if s.startswith(prefix)]
```