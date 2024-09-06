```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    >>> filter_by_prefix([('ab', 'cd'), ('abc', 'cde'), 'array'], 'a')
    ['ab', 'abc', 'array']

    >>> filter_by_prefix([1, 2, 3, 'abc', 'cde'], 'id')
    []

    >>> filter_by_prefix(['abcde', 'abcd', 'bc'], 'a')
    ['abc', 'abcd']
    """
    return [x for x in strings if prefix == x[0]]
```