```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ bands 🌴, 🌟], 'om')
    ['🌴']
    """
    return [string for string in strings if string.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It uses a approach of list comprehension to filter out any elements that don't start with the given prefix, then returns the list of matching strings.