```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    >>> filter_by_prefix([ 'def', 'gHI', 'jkl', 'wxy'], 'j')
    []
    """
    return [x for x in strings if x.startswith(prefix)]
```

This code defines a function called `filter_by_prefix`, which takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the given prefix.