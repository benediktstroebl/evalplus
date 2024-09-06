Here is a Python script that includes a self-contained function that filters an input list of strings for those starting with a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings, keeping only those starting with the prefix.
    >>> filter_by_prefix([ acting, tech ], 'acting')
    ['acting']
    >>> filter_by_prefix([12, 23, 45, 56, 67,89], '12')
    [12, 56]
    >>> filter_by_prefix([abc, bcd, cde, array], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if prefix == x[0]]
```