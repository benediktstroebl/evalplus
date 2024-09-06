```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([('apple', 'banana'), ('carrot', 'spinach'), ('crisp', 'pretation')], 'apple')
    ['apple', 'carrot', 'crisp']

    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd')
    []
    """
    return [string for string in strings if string[0] == prefix]
```