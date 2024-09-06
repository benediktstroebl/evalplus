Here is a self-contained Python script that includes a function `filter_by_prefix` which solves the problem of filtering strings by their prefix:

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function that takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the given prefix.