```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa'])
    Trace [](): Type 'List[str]' is not implicitly convertible to 'Optional[str]'
    """
    return next((x for x in strings if len(x) == len(strings[0])), None)
```