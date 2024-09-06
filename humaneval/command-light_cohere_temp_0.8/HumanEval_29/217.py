Here is a self-contained Python script that defines a function `filter_by_prefix` solving the problem you have described:

```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([abc, 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]
```

This script provides a function that takes a list of strings and a prefix, and returns a new list containing only the strings from the input list that start with the given prefix.