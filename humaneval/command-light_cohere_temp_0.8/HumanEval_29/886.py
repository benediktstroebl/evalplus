Certainly! Here's the Python script that provides the solution to the problem you described:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with the given prefix. It uses a idealization to check whether each string starts with the prefix and then filters the list accordingly.