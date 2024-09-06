```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ 'abc', 'bcde', 'cdef', 'array', 'aabb'], 'a')
    ['abc', 'aabb']
    """
    return [x for x in strings if x.startswith(prefix)]
```